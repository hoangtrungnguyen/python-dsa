import React, { useState, useEffect, useRef } from 'react';

// Main App component
const App = () => {
  // State to hold the WebSocket instance
  const ws = useRef(null);
  // State to hold the generated arithmetic operation string
  const [currentOperation, setCurrentOperation] = useState('');
  // State to hold the log of messages (sent and received)
  const [messageLog, setMessageLog] = useState([]);
  // State for WebSocket connection status
  const [isConnected, setIsConnected] = useState(false);

  // Drawing-specific states
  const canvasRef = useRef(null); // Ref to the canvas element
  const [isDrawing, setIsDrawing] = useState(false); // Flag to indicate if drawing is active
  const [lastPoint, setLastPoint] = useState({ x: 0, y: 0 }); // Last recorded point for drawing a line segment
  const [currentPath, setCurrentPath] = useState([]); // Array to store points of the current drawing stroke

  // Effect hook to establish and manage the WebSocket connection
  useEffect(() => {
    // Attempt to connect to the WebSocket server
    // For this example, we assume a server is running at ws://localhost:8080.
    ws.current = new WebSocket('ws://localhost:8080');

    // WebSocket onopen event handler: Fired when the connection is established
    ws.current.onopen = () => {
      console.log('WebSocket connected');
      setIsConnected(true);
      setMessageLog((prevLog) => [...prevLog, { type: 'system', text: 'Connected to WebSocket server.' }]);
    };

    // WebSocket onmessage event handler: Fired when a message is received from the server
    ws.current.onmessage = (event) => {
      console.log('Message from server:', event.data);
      setMessageLog((prevLog) => [...prevLog, { type: 'received', text: `Server: ${event.data}` }]);
    };

    // WebSocket onerror event handler: Fired when an error occurs
    ws.current.onerror = (error) => {
      console.error('WebSocket error:', error);
      setMessageLog((prevLog) => [...prevLog, { type: 'error', text: 'WebSocket error occurred.' }]);
    };

    // WebSocket onclose event handler: Fired when the connection is closed
    ws.current.onclose = () => {
      console.log('WebSocket disconnected');
      setIsConnected(false);
      setMessageLog((prevLog) => [...prevLog, { type: 'system', text: 'Disconnected from WebSocket server.' }]);
      // Optional: Implement reconnection logic here if needed, though not in this example.
    };

    // Cleanup function: Fired when the component unmounts or dependencies change
    // This ensures the WebSocket connection is properly closed to prevent memory leaks
    return () => {
      if (ws.current) {
        ws.current.close();
      }
    };
  }, []); // Empty dependency array means this effect runs only once on mount

  // Effect hook for canvas initialization and resizing
  useEffect(() => {
    const canvas = canvasRef.current;
    if (!canvas) return; // Ensure canvas element exists
    const ctx = canvas.getContext('2d');

    // Set default drawing styles
    ctx.lineCap = 'round';
    ctx.strokeStyle = '#FFFFFF'; // White drawing color for visibility on dark background
    ctx.lineWidth = 2; // Default line width

    // Function to handle canvas resizing to fill its container
    const resizeCanvas = () => {
      const rect = canvas.getBoundingClientRect();
      // Set the canvas's internal resolution to match its display size
      canvas.width = rect.width;
      canvas.height = rect.height;
      // Reapply styles after resizing as canvas clear them
      ctx.lineCap = 'round';
      ctx.strokeStyle = '#FFFFFF';
      ctx.lineWidth = 2;
    };

    // Initial resize call
    resizeCanvas();
    // Add event listener for window resize to make canvas responsive
    window.addEventListener('resize', resizeCanvas);

    // Cleanup function for the canvas resize listener
    return () => {
      window.removeEventListener('resize', resizeCanvas);
    };
  }, []); // Empty dependency array means this effect runs only once on mount

  // Function to generate a random arithmetic operation and send it via WebSocket
  const generateAndSendArithmeticOperation = () => {
    if (ws.current && ws.current.readyState === WebSocket.OPEN) {
      // Define possible operations
      const operations = ['ADD', 'SUBTRACT', 'MULTIPLY', 'DIVIDE'];
      // Select a random operation
      const randomOperation = operations[Math.floor(Math.random() * operations.length)];
      // Generate two random numbers between 1 and 100
      const num1 = Math.floor(Math.random() * 100) + 1;
      const num2 = Math.floor(Math.random() * 100) + 1;

      // Construct the operation object
      const operationData = {
        id: Date.now(), // Unique ID for the operation
        type: randomOperation, // Type of operation (e.g., 'ADD')
        operands: [num1, num2], // Numbers involved in the operation
        timestamp: new Date().toISOString(), // Timestamp of creation
      };

      // Convert the operation object to a JSON string
      const message = JSON.stringify(operationData);

      try {
        // Send the message over the WebSocket
        ws.current.send(message);
        console.log('Sent arithmetic operation:', operationData);
        // Update the current operation display
        setCurrentOperation(`${randomOperation} ${num1} and ${num2}`);
        // Add the sent message to the log
        setMessageLog((prevLog) => [...prevLog, { type: 'sent', text: `Sent: ${message}` }]);
      } catch (error) {
        console.error('Failed to send arithmetic message:', error);
        setMessageLog((prevLog) => [...prevLog, { type: 'error', text: `Failed to send: ${message}` }]);
      }
    } else {
      setMessageLog((prevLog) => [...prevLog, { type: 'system', text: 'WebSocket is not connected. Please ensure the server is running.' }]);
      console.warn('WebSocket is not connected.');
    }
  };

  // Drawing event handlers
  const startDrawing = ({ nativeEvent }) => {
    // ALLOW drawing regardless of connection status
    const { offsetX, offsetY } = nativeEvent; // Get coordinates relative to the canvas
    setIsDrawing(true);
    setLastPoint({ x: offsetX, y: offsetY });
    setCurrentPath([{ x: offsetX, y: offsetY }]); // Start a new path with the initial point
  };

  const draw = ({ nativeEvent }) => {
    if (!isDrawing) return; // Only draw if the mouse button is pressed
    const canvas = canvasRef.current;
    const ctx = canvas.getContext('2d');
    const { offsetX, offsetY } = nativeEvent;

    // Begin a new path for drawing a line segment
    ctx.beginPath();
    // Move to the last recorded point
    ctx.moveTo(lastPoint.x, lastPoint.y);
    // Draw a line to the current mouse position
    ctx.lineTo(offsetX, offsetY);
    // Stroke the line
    ctx.stroke();

    // Update the last point to the current position
    setLastPoint({ x: offsetX, y: offsetY });
    // Add the current point to the path being accumulated
    setCurrentPath((prevPath) => [...prevPath, { x: offsetX, y: offsetY }]);
  };

  const stopDrawing = () => {
    setIsDrawing(false);
    // Only send the path if actual drawing occurred (more than one point)
    if (currentPath.length > 1) {
      sendDrawingOperation(currentPath);
    }
    setCurrentPath([]); // Clear the current path for the next stroke
  };

  // Function to send drawing data via WebSocket
  const sendDrawingOperation = (path) => {
    // Only attempt to send if connected
    if (ws.current && ws.current.readyState === WebSocket.OPEN) {
      const canvas = canvasRef.current;
      const operationData = {
        id: Date.now(),
        type: "DRAWING", // Specific type for drawing operations
        data: {
          path: path, // Array of points representing the stroke
          canvasWidth: canvas.width, // Canvas width at the time of drawing
          canvasHeight: canvas.height, // Canvas height at the time of drawing
          color: canvas.getContext('2d').strokeStyle, // Color used for drawing
          lineWidth: canvas.getContext('2d').lineWidth // Line width used for drawing
        },
        timestamp: new Date().toISOString(),
      };
      const message = JSON.stringify(operationData);

      try {
        ws.current.send(message);
        console.log('Sent drawing operation:', operationData);
        // Log a truncated version of the path for brevity
        setMessageLog((prevLog) => [...prevLog, { type: 'sent', text: `Sent Drawing: Path length ${operationData.data.path.length}.` }]);
      } catch (error) {
        console.error('Failed to send drawing message:', error);
        setMessageLog((prevLog) => [...prevLog, { type: 'error', text: `Failed to send drawing: ${error.message}` }]);
      }
    } else {
      // If not connected, inform the user that the drawing won't be sent
      setMessageLog((prevLog) => [...prevLog, { type: 'system', text: 'Drawing created locally, but WebSocket is not connected to send it.' }]);
    }
  };

  // Function to clear the canvas
  const clearCanvas = () => {
    const canvas = canvasRef.current;
    if (canvas) {
      const ctx = canvas.getContext('2d');
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      setMessageLog((prevLog) => [...prevLog, { type: 'system', text: 'Canvas cleared.' }]);
    }
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-indigo-500 to-purple-600 flex flex-col items-center justify-center p-4 font-inter text-white">
      <div className="bg-white bg-opacity-10 rounded-xl shadow-2xl p-8 max-w-4xl w-full backdrop-blur-sm border border-white border-opacity-20 flex flex-col items-center">
        <h1 className="text-4xl font-bold mb-6 text-center">Operation Sender</h1>

        {/* Connection Status */}
        <div className={`px-4 py-2 rounded-full text-sm font-semibold mb-6 ${isConnected ? 'bg-green-500' : 'bg-red-500'}`}>
          Status: {isConnected ? 'Connected' : 'Disconnected'}
        </div>

        {/* Arithmetic Operation Section */}
        <div className="mb-8 w-full text-center">
          <h2 className="text-2xl font-semibold mb-4">Arithmetic Operations</h2>
          <div className="mb-6 w-full text-center">
            <p className="text-lg mb-2">Current Operation:</p>
            <div className="bg-white bg-opacity-20 rounded-lg p-4 text-xl font-mono break-words">
              {currentOperation || 'No arithmetic operation sent yet.'}
            </div>
          </div>
          <button
            onClick={generateAndSendArithmeticOperation}
            className="bg-blue-500 hover:bg-blue-600 active:bg-blue-700 text-white font-bold py-3 px-6 rounded-full shadow-lg transform transition duration-200 ease-in-out hover:scale-105 disabled:opacity-50 disabled:cursor-not-allowed"
            disabled={!isConnected}
          >
            Generate & Send Arithmetic Operation
          </button>
        </div>

        {/* Drawing Section */}
        <div className="mb-8 w-full text-center">
          <h2 className="text-2xl font-semibold mb-4">Drawing Space</h2>
          <div className="relative w-full aspect-video bg-gray-800 bg-opacity-50 rounded-lg shadow-inner overflow-hidden mb-4 border border-white border-opacity-20">
            <canvas
              ref={canvasRef}
              onMouseDown={startDrawing}
              onMouseMove={draw}
              onMouseUp={stopDrawing}
              onMouseLeave={stopDrawing} // Stop drawing if mouse leaves canvas
              className="w-full h-full cursor-crosshair"
            >
              Your browser does not support the HTML canvas tag.
            </canvas>
          </div>
          <button
            onClick={clearCanvas}
            className="bg-red-500 hover:bg-red-600 active:bg-red-700 text-white font-bold py-2 px-5 rounded-full shadow-lg transform transition duration-200 ease-in-out hover:scale-105"
            // Clear canvas button is always enabled
          >
            Clear Drawing
          </button>
        </div>


        {/* Message Log */}
        <div className="mt-4 w-full bg-white bg-opacity-10 rounded-lg p-4 max-h-60 overflow-y-auto border border-white border-opacity-20">
          <h2 className="text-xl font-semibold mb-4 text-center">Message Log</h2>
          <div className="space-y-2">
            {messageLog.length === 0 ? (
              <p className="text-gray-300 text-center">No messages yet.</p>
            ) : (
              messageLog.map((msg, index) => (
                <p key={index} className={`p-2 rounded-md text-sm break-words ${
                  msg.type === 'sent' ? 'bg-purple-700 bg-opacity-30' :
                  msg.type === 'received' ? 'bg-green-700 bg-opacity-30' :
                  msg.type === 'error' ? 'bg-red-700 bg-opacity-30' :
                  'bg-gray-700 bg-opacity-30'
                }`}>
                  {msg.text}
                </p>
              ))
            )}
          </div>
        </div>
      </div>
    </div>
  );
};

export default App;
