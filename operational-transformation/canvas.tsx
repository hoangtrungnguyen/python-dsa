import React, { useRef, useEffect, useState, useCallback } from 'react';
import { initializeApp } from 'firebase/app';
import { getAuth, signInAnonymously, signInWithCustomToken, onAuthStateChanged } from 'firebase/auth';
import { getFirestore, doc, getDoc, addDoc, setDoc, updateDoc, deleteDoc, onSnapshot, collection, query, where, addDoc, getDocs, orderBy } from 'firebase/firestore';

// Global variables provided by the Canvas environment
const appId = typeof __app_id !== 'undefined' ? __app_id : 'default-app-id';
const firebaseConfig = typeof __firebase_config !== 'undefined' ? JSON.parse(__firebase_config) : {};
const initialAuthToken = typeof __initial_auth_token !== 'undefined' ? __initial_auth_token : null;

// Define the structure for a drawing operation
// This is crucial for efficient data storage and real-time updates.
// Instead of sending the whole canvas image, we send commands.
/**
 * @typedef {Object} DrawingOperation
 * @property {string} type - Type of drawing operation (e.g., 'line', 'clear').
 * @property {string} color - Hex color code.
 * @property {number} lineWidth - Line width.
 * @property {Array<{x: number, y: number}>} points - Array of points for line segments.
 * @property {number} timestamp - Timestamp of the operation, used for ordering.
 * @property {string} userId - ID of the user who performed the operation.
 */

function App() {
  const canvasRef = useRef(null);
  const [isDrawing, setIsDrawing] = useState(false);
  const [currentColor, setCurrentColor] = useState('#000000');
  const [lineWidth, setLineWidth] = useState(5);
  const [drawingData, setDrawingData] = useState([]); // Stores all drawing operations
  const [db, setDb] = useState(null);
  const [auth, setAuth] = useState(null);
  const [userId, setUserId] = useState('Loading...'); // Display current user ID
  const [isAuthReady, setIsAuthReady] = useState(false); // Flag to ensure Firestore ops happen after auth

  // 1. Initialize Firebase and Authenticate User
  useEffect(() => {
    try {
      const app = initializeApp(firebaseConfig);
      const firestore = getFirestore(app);
      const firebaseAuth = getAuth(app);

      setDb(firestore);
      setAuth(firebaseAuth);

      const unsubscribe = onAuthStateChanged(firebaseAuth, async (user) => {
        if (user) {
          setUserId(user.uid);
          setIsAuthReady(true);
          console.log("Firebase Auth State Changed: Logged in as", user.uid);
        } else {
          try {
            // Sign in with custom token if available, otherwise anonymously
            if (initialAuthToken) {
              await signInWithCustomToken(firebaseAuth, initialAuthToken);
              console.log("Signed in with custom token.");
            } else {
              await signInAnonymously(firebaseAuth);
              console.log("Signed in anonymously.");
            }
          } catch (error) {
            console.error("Firebase authentication error:", error);
            setUserId('Auth Error');
            setIsAuthReady(true); // Still set ready to allow UI to render even if auth fails
          }
        }
      });
      return () => unsubscribe(); // Cleanup auth listener
    } catch (error) {
      console.error("Error initializing Firebase:", error);
      setUserId('Init Error');
      setIsAuthReady(true); // Set ready to allow UI to render even if init fails
    }
  }, []);

  // 2. Set up Firestore Listener for Real-time Updates
  // This listens for new drawing operations from any session and updates the canvas.
  useEffect(() => {
    if (!db || !isAuthReady) return; // Wait for Firebase and auth to be ready

    // Define the collection path for public data
    const drawingsCollectionRef = collection(db, `artifacts/${appId}/public/data/drawings`);
    console.log("Attempting to listen to Firestore collection:", `artifacts/${appId}/public/data/drawings`);

    // Listen for real-time updates
    const unsubscribe = onSnapshot(drawingsCollectionRef, (snapshot) => {
      const newDrawingOperations = [];
      snapshot.docChanges().forEach((change) => {
        const data = change.doc.data();
        if (data.points && Array.isArray(data.points)) { // Ensure points is an array
          newDrawingOperations.push({ id: change.doc.id, ...data });
        } else {
            console.warn("Skipping invalid drawing operation:", data);
        }
      });

      // Sort operations by timestamp to ensure correct drawing order
      newDrawingOperations.sort((a, b) => a.timestamp - b.timestamp);

      // Merge new operations with existing ones, avoiding duplicates by ID
      setDrawingData(prevData => {
        const updatedData = new Map(prevData.map(op => [op.id, op]));
        newDrawingOperations.forEach(op => updatedData.set(op.id, op));
        return Array.from(updatedData.values()).sort((a, b) => a.timestamp - b.timestamp);
      });
      console.log("Received updates from Firestore. Total operations:", newDrawingOperations.length);
    }, (error) => {
      console.error("Error listening to Firestore:", error);
    });

    return () => unsubscribe(); // Cleanup Firestore listener
  }, [db, isAuthReady]); // Re-run if db or auth state changes

  // 3. Drawing Logic
  const drawOperation = useCallback((ctx, operation) => {
    ctx.strokeStyle = operation.color;
    ctx.lineWidth = operation.lineWidth;
    ctx.lineCap = 'round';
    ctx.lineJoin = 'round';

    if (operation.type === 'line' && operation.points && operation.points.length > 1) {
      ctx.beginPath();
      ctx.moveTo(operation.points[0].x, operation.points[0].y);
      for (let i = 1; i < operation.points.length; i++) {
        ctx.lineTo(operation.points[i].x, operation.points[i].y);
      }
      ctx.stroke();
    } else if (operation.type === 'clear') {
      ctx.clearRect(0, 0, ctx.canvas.width, ctx.canvas.height);
    }
  }, []);

  // Redraw the entire canvas based on current drawingData
  useEffect(() => {
    const canvas = canvasRef.current;
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    if (!ctx) return;

    // Clear canvas before redrawing all operations
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    drawingData.forEach(op => drawOperation(ctx, op));
    console.log("Canvas redrawn with", drawingData.length, "operations.");
  }, [drawingData, drawOperation]);

  // Handle Mouse/Touch Events for Drawing
  const handleMouseDown = useCallback((e) => {
    if (!canvasRef.current || !userId || userId === 'Loading...') return;
    setIsDrawing(true);
    const canvas = canvasRef.current;
    const rect = canvas.getBoundingClientRect();
    const x = e.clientX - rect.left;
    const y = e.clientY - rect.top;

    // Start a new line operation
    const newOperation = {
      type: 'line',
      color: currentColor,
      lineWidth: lineWidth,
      points: [{ x, y }],
      timestamp: Date.now(),
      userId: userId,
    };
    // Add locally immediately for responsiveness
    setDrawingData(prev => [...prev, newOperation]);
  }, [currentColor, lineWidth, userId]);

  const handleMouseMove = useCallback((e) => {
    if (!isDrawing || !canvasRef.current || !userId || userId === 'Loading...') return;

    const canvas = canvasRef.current;
    const rect = canvas.getBoundingClientRect();
    const x = e.clientX - rect.left;
    const y = e.clientY - rect.top;

    setDrawingData(prevData => {
      const lastOperationIndex = prevData.length - 1;
      if (lastOperationIndex < 0 || prevData[lastOperationIndex].type !== 'line' || prevData[lastOperationIndex].userId !== userId) {
        // This case should ideally not happen if handleMouseDown correctly starts a line
        return prevData;
      }
      const updatedData = [...prevData];
      updatedData[lastOperationIndex] = {
        ...updatedData[lastOperationIndex],
        points: [...updatedData[lastOperationIndex].points, { x, y }],
        timestamp: Date.now(), // Update timestamp to ensure latest operation on drag
      };
      return updatedData;
    });
  }, [isDrawing, userId]);

  const handleMouseUp = useCallback(async () => {
    setIsDrawing(false);
    if (!db || !userId || userId === 'Loading...') return;

    // Persist the completed drawing operation to Firestore
    const lastOperation = drawingData[drawingData.length - 1];
    if (lastOperation && lastOperation.userId === userId && lastOperation.type === 'line' && lastOperation.points.length > 1) {
      try {
        const drawingsCollectionRef = collection(db, `artifacts/${appId}/public/data/drawings`);
        // Remove the temporary ID added during local drawing before saving to Firestore
        const { id, ...operationToSave } = lastOperation;
        await addDoc(drawingsCollectionRef, operationToSave);
        console.log("Drawing operation added to Firestore.");
      } catch (e) {
        console.error("Error adding document: ", e);
      }
    }
  }, [isDrawing, db, userId, drawingData]);

  const handleMouseLeave = useCallback(() => {
    if (isDrawing) {
      handleMouseUp();
    }
  }, [isDrawing, handleMouseUp]);


  // Function to clear the canvas and send a clear operation to Firestore
  const clearCanvas = async () => {
    if (!db || !userId || userId === 'Loading...') return;

    const clearOperation = {
      type: 'clear',
      color: '#000000', // Color doesn't matter for clear, but keep for consistency
      lineWidth: 1,      // Line width doesn't matter for clear
      points: [],        // No points needed for clear
      timestamp: Date.now(),
      userId: userId,
    };

    try {
      const drawingsCollectionRef = collection(db, `artifacts/${appId}/public/data/drawings`);
      await addDoc(drawingsCollectionRef, clearOperation);
      console.log("Clear operation sent to Firestore.");
    } catch (e) {
      console.error("Error sending clear operation: ", e);
    }
  };

  // Resize canvas to fit screen
  useEffect(() => {
    const canvas = canvasRef.current;
    if (canvas) {
      const setCanvasDimensions = () => {
        canvas.width = canvas.offsetWidth;
        canvas.height = canvas.offsetHeight;
        // Redraw content after resize
        const ctx = canvas.getContext('2d');
        if (ctx) {
            ctx.clearRect(0, 0, canvas.width, canvas.height);
            drawingData.forEach(op => drawOperation(ctx, op));
        }
      };

      // Set initial size
      setCanvasDimensions();
      // Add resize listener
      window.addEventListener('resize', setCanvasDimensions);
      // Clean up
      return () => window.removeEventListener('resize', setCanvasDimensions);
    }
  }, [drawingData, drawOperation]); // Redraw when drawingData changes, to maintain content after resize

  return (
    <div className="flex flex-col items-center justify-center min-h-screen bg-gray-100 p-4 font-inter text-gray-800">
      <h1 className="text-4xl font-extrabold text-blue-700 mb-6 drop-shadow-md">Collaborative Canvas</h1>
      <p className="text-lg mb-4">
        Your User ID: <span className="font-semibold text-purple-600">{userId}</span>
      </p>

      <div className="flex flex-col md:flex-row items-center space-y-4 md:space-y-0 md:space-x-6 mb-6 p-4 bg-white rounded-xl shadow-lg">
        <div className="flex items-center space-x-3">
          <label htmlFor="colorPicker" className="text-gray-700 font-medium">Color:</label>
          <input
            type="color"
            id="colorPicker"
            value={currentColor}
            onChange={(e) => setCurrentColor(e.target.value)}
            className="w-16 h-10 rounded-lg border-2 border-gray-300 cursor-pointer transition duration-300 ease-in-out hover:border-blue-500 focus:outline-none focus:ring-2 focus:ring-blue-400"
          />
        </div>
        <div className="flex items-center space-x-3">
          <label htmlFor="lineWidthSlider" className="text-gray-700 font-medium">Line Width: {lineWidth}</label>
          <input
            type="range"
            id="lineWidthSlider"
            min="1"
            max="20"
            value={lineWidth}
            onChange={(e) => setLineWidth(parseInt(e.target.value))}
            className="w-32 h-2 bg-gray-300 rounded-lg appearance-none cursor-pointer accent-blue-500 focus:outline-none focus:ring-2 focus:ring-blue-400"
          />
        </div>
        <button
          onClick={clearCanvas}
          className="px-6 py-2 bg-red-500 text-white font-semibold rounded-lg shadow-md hover:bg-red-600 transition duration-300 ease-in-out transform hover:scale-105 focus:outline-none focus:ring-2 focus:ring-red-400 focus:ring-opacity-75"
        >
          Clear Canvas
        </button>
      </div>

      <div className="w-full max-w-4xl h-96 bg-white rounded-xl shadow-xl border-4 border-blue-400 overflow-hidden">
        <canvas
          ref={canvasRef}
          className="w-full h-full block"
          onMouseDown={handleMouseDown}
          onMouseMove={handleMouseMove}
          onMouseUp={handleMouseUp}
          onMouseLeave={handleMouseLeave}
          // Add touch events for mobile responsiveness
          onTouchStart={(e) => {
            e.preventDefault(); // Prevent scrolling
            const touch = e.touches[0];
            handleMouseDown(touch);
          }}
          onTouchMove={(e) => {
            e.preventDefault(); // Prevent scrolling
            const touch = e.touches[0];
            handleMouseMove(touch);
          }}
          onTouchEnd={handleMouseUp}
        >
          Your browser does not support the HTML canvas tag.
        </canvas>
      </div>

      <p className="mt-6 text-sm text-gray-500">
        Draw on the canvas. Your strokes will be synchronized with other connected sessions in real-time!
      </p>
    </div>
  );
}

export default App;
