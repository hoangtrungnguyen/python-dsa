# import socket
# import collections
# import pickle
# import time
#
# from flask import  Flask, request
# from flask_socketio import SocketIO, emit, leave_room, join_room
# from document import Document
# from operation import Operation
# from network_utils import receive_pickled_data, send_pickled_data
#
#
# # Initialize Flask app
# app = Flask(__name__)
#
# # Configure SocketIO: async_mode='threading' is suitable for simple demos;
# # for production, consider 'eventlet' or 'gevent' for better performance.
# socketio = SocketIO(app, cors_allowed_origins="*", async_mode='threading')
# class Server:
#
#     def __init__(self, initial_text:str):
#         self.document = Document(initial_text)
#         self.version = 0 # Canonical version number of the document
#         self.history = [] # Stores all operations applied in canonical order
#         # Map SocketIO sid to our custom client_id (e.g., "Client-A")
#         self.sid_to_client_id = {}
#         self.client_id_to_sid = {} # Map custom client_id back to sid for direct emit
#         self.lock = threading.Lock() # Lock for critical sections (document, history, version)
#         self.room_name = "document_room" # All clients join this room for broadcast
#
#
#     def init_document(self):
#         pass
#     def _transform(self, op1: Operation, op2: Operation) -> Operation:
#         pass
#
#     # def receive_operation(self, ):
#
#
#     def process_and_broadcast_operation(self, client_op: Operation, client_version: int):
#         print(f"Start processing data from {client_op.client_id} - version: {client_version}")
#         pass
#         """
# Server receives an operation from a client.
# 1. Transforms the client_op against server's history (operations client hasn't seen).
# 2. Applies the transformed operation to its canonical document.
# 3. Appends the transformed operation to its history.
# 4. Increments its version.
# 5. Broadcasts the transformed operation and new server version to ALL connected clients.
#         """
#         print(f"\nSERVER: Received op {client_op} from client {client_op.client_id} at client_version {client_version}")
#         print(f"SERVER: Current canonical document: '{self.document}' (v{self.version})")
#
#         # 1. Transform client_op against serve
#         # The client_op needs to be rebased against all operations that the server
#         # has applied *since* the client created its operation.
#         transformed_op = Operation(client_op.operation_type, client_op.pos, client_op.value, client_op.client_id, client_op.client_version)
#         # Get operations from history that client hasn't seen yet
#         # These are operations applied to the server's document *after* client_op was created.
#         server_ops_since_client_op_base = self.history[client_version:]
#
#         pass
#
#
#
#
#
