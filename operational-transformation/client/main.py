import socket
import threading
import collections
import pickle
import time

from document import Document
from operation import Operation
from network_utils import send_pickled_data, receive_pickled_data


class ServerEmulator:
    def _transform(self, op1: Operation, op2: Operation):
        pass
class Client:
    """
Simulates a collaborative editing client (user's local editor).
Applies operations optimistically, manages pending operations,
and rebases local state based on server acknowledgments and remote operations.
    """
    def __init__(self, id: str, host: str, port: int):
        self.id = id
        self.document = Document("") # Initialized by server sync
        self.server_version = 0
        self.pending_operations = collections.deque()
        self.server_emulator = ServerEmulator() # For client-side transformation logic

        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = host
        self.port = port
        self.connected = False
        self.connect_to_server()

        # Start a thread to continuously listen for server responses
        self.listener_thread = threading.Thread(target=self._listen_for_server_responses, daemon=True)
        self.listener_thread.start()
    def connect_to_server(self):
        """Attempts to connect to the server."""
        try:
            self.client_socket.connect((self.host, self.port))
            self.connected = True
            print(f"CLIENT {self.id}: Connected to server at {self.host}:{self.port}")
        except ConnectionRefusedError:
            print(f"CLIENT {self.id}: Connection refused. Is server running?")
        except Exception as e:
            print(f"CLIENT {self.id}: Error connecting to server: {e}")

    def _listen_for_server_responses(self):
        """Continuously listens for data from the server."""
        while self.connected:
            try:
                server_data, new_server_version = receive_pickled_data(self.client_socket)
                self._process_server_response(server_data, new_server_version)
            except EOFError:
                print(f"CLIENT {self.id}: Server disconnected.")
                self.connected = False
                break
            except Exception as e:
                print(f"CLIENT {self.id}: Error receiving from server: {e}")
                self.connected = False
                break
        self.client_socket.close()

    def _process_server_response(self, server_data, new_server_version: int):
        print(f'server_data {server_data}')
        print(f'new_server_version {new_server_version}')


    def make_change(self,op_type:str,pos:int, value):
        if not self.connected:
            print(f"CLIENT {self.id}: Not connected to server. Cannot make change.")
            return
        op = Operation(op_type, pos, value, self.id, self.server_version)
        print(f"\nCLIENT {self.id}: Local state (v{self.server_version} + {len(self.pending_operations)} pending) before change: '{self.document}'")
        

def run_client(client_id, host, port, actions):
    client = Client(client_id, host, port)
    if not client.connected:
        return

    # Give some time for initial sync
    time.sleep(1)

    for action in actions:
        if action[0] == 'sleep':
            print(f"\nCLIENT {client_id}: Sleeping for {action[1]} seconds...")
            time.sleep(action[1])
        else:
            client.make_change(action[0], action[1], action[2])
            time.sleep(0.1) # Small delay to allow server to process and broadcast

if __name__ == "__main__":
    SERVER_HOST = '127.0.0.1'
    SERVER_PORT = 65432

    # Define actions for Client A
    actions_a = [
        ('insert', 4, "A_Insert_"), # "The A_Insert_quick brown fox..."
        ('sleep', 2),
        ('delete', 15, 5), # Delete 'brown'
        ('sleep', 3),
        ('insert', 0, "START_"),
        ('sleep', 1)
    ]

    # Define actions for Client B (concurrent with A)
    actions_b = [
        ('sleep', 0.5), # Start slightly after A
        ('insert', 10, "_B_Insert_"), # "The quick _B_Insert_brown fox..."
        ('sleep', 1),
        ('delete', 20, 3), # Delete 'fox'
        ('sleep', 2),
        ('insert', 20, "_END_")
    ]

    # Start clients in separate threads
    thread_a = threading.Thread(target=run_client, args=("Client-A", SERVER_HOST, SERVER_PORT, actions_a))
    thread_b = threading.Thread(target=run_client, args=("Client-B", SERVER_HOST, SERVER_PORT, actions_b))

    thread_a.start()
    thread_b.start()

    # Keep main thread alive to allow client threads to run
    thread_a.join()
    thread_b.join()

    print("\n--- All client operations simulated ---")
    print("Please check server_app.py output for final canonical document state.")
