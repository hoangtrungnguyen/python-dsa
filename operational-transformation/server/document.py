from operation import Operation

class Document:
    """
Represents the text document that is being edited.
Provides a simple apply method for operations.
    """
    def __init__(self, text: str = ""):
        self.text = text

    def apply(self, op: Operation):
        """Applies an operation to the document's text."""
        if op.operation_type == 'insert':
            # Ensure position is within bounds
            insert_pos = min(max(0, op.pos), len(self.text))
            self.text = self.text[:insert_pos] + op.value + self.text[insert_pos:]
        elif op.operation_type == 'delete':
            # Ensure position and length are valid for deletion
            start_pos = min(max(0, op.pos), len(self.text))
            delete_length = min(op.value, len(self.text) - start_pos)

            if delete_length > 0:
                self.text = self.text[:start_pos] + self.text[start_pos + delete_length:]
            # If delete_length is 0 or less, it's a no-op, no change to text
        elif op.operation_type == 'noop':
            pass # No operation to apply
        else:
            print(f"Error: Unknown operation type: {op.operation_type}")

    def __str__(self):
        """Returns the current text of the document."""
        return self.text

class Component:
    def __init__(self, x: int , y: int ):
        self.x = x
        self.y = y

