from document import Document
from operation import Operation

class Client:

    def __init__(self, document: Document):
        self.document = document


    def init(self):
        """
        1. Open socket to server 
        2. Initialize document"""
        pass


    def insert(self):
        pass

    def delete(self):
        pass


    def apply_local(self):
        pass


    def consume_remote_op(self):
        pass

    def _transform(self, server_op: Operation):
        pass