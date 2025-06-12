class Operation:
    """
Represents a single text editing operation.
'insert': inserts a string at a position.
'delete': deletes a number of characters starting at a position.
    """
    def __init__(self, operation_type: str, pos: int, value, client_id: str = None, client_version: int = None):
        self.operation_type = operation_type # 'insert', 'delete', or 'noop' (for transformed ops that become null)
        self.pos = pos
        self.value = value # string for insert, int for delete (length)
        self.client_id = client_id # Identifier of the client that created this op
        self.client_version = client_version # Server version client based this op on

    def __repr__(self):
        """String representation of the operation."""
        return f"Op({self.operation_type}, pos={self.pos}, val={repr(self.value)}, client={self.client_id}@{self.client_version})"

    def __eq__(self, other):
        """Equality check for operations (for simple demo purposes)."""
        if not isinstance(other, Operation):
            return NotImplemented
        return (self.operation_type == other.operation_type and
                self.pos == other.pos and
                self.value == other.value and
                self.client_id == other.client_id and
                self.client_version == other.client_version)

    def __hash__(self):
        """Hash for operations (needed for equality checks in some contexts)."""
        return hash((self.operation_type, self.pos, self.value, self.client_id, self.client_version))