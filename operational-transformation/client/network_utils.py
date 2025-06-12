import socket
import pickle

def send_pickled_data(sock: socket.socket, data):
    """
Sends a Python object over a socket after pickling it.
:param sock: The socket to send data over.
:param data: The Python object to send.
    """
    try:
        pickled_data = pickle.dumps(data)
        # Prepend the length of the pickled data to the message
        # This helps the receiver know how many bytes to expect for a complete object.
        length_prefix = len(pickled_data).to_bytes(4, 'big') # 4 bytes for length
        sock.sendall(length_prefix + pickled_data)
    except (BrokenPipeError, ConnectionResetError) as e:
        print(f"Network error sending data: {e}")
        raise # Re-raise to be handled by caller
    except Exception as e:
        print(f"Error pickling or sending data: {e}")
        raise

def receive_pickled_data(sock: socket.socket):
    """
Receives pickled Python object from a socket.
Assumes the sender prepends a 4-byte length prefix.
:param sock: The socket to receive data from.
:return: The unpickled Python object.
:raises EOFError: If the socket is closed unexpectedly.
:raises pickle.UnpicklingError: If the received data is corrupted or incomplete.
    """
    raw_length = b""
    while len(raw_length) < 4:
        chunk = sock.recv(4 - len(raw_length))
        if not chunk:
            raise EOFError("Socket disconnected while waiting for length prefix.")
        raw_length += chunk

    message_length = int.from_bytes(raw_length, 'big')

    data_buffer = b""
    while len(data_buffer) < message_length:
        chunk = sock.recv(message_length - len(data_buffer))
        if not chunk:
            raise EOFError("Socket disconnected while waiting for message data.")
        data_buffer += chunk

    return pickle.loads(data_buffer)

    