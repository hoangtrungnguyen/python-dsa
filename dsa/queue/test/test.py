
# Test cases
test_cases = [
    ([], []),  # Empty queue
    ([1, 2, 3], []),  # Push onto empty stack1
    ([], [3, 2, 1]),  # Push onto empty stack2 (simulates previous pops)
    ([1, 2], [4, 5]),  # Push with both stacks non-empty
    ([1], [3]),  # Push with both stacks having one element
]


def test_double_stack_queue(operations, expected_output):
    queue = DoubleStackQueue()
    actual_output = []
    for op, val in operations:
        if op == "push":
            queue.push(val)
        elif op == "pop":
            actual_output.append(queue.pop())
        elif op == "peek":
            actual_output.append(queue.peek())
        elif op == "empty":
            actual_output.append(queue.empty())
    if actual_output != expected_output:
        print("Error:")
        print("Operations:", operations)
        print("Expected Output:", expected_output)
        print("Actual Output:", actual_output)


# Test suite (combination of operations for each test case)
operations_suite = [
    [("push", 1), ("push", 2), ("peek", None), ("pop", None), ("empty", None)],
    [("push", 1), ("pop", None), ("empty", None)],
    [("pop", None), ("push", 1), ("peek", None)],  # Pop from empty, then push and peek
    [("push", 1), ("push", 2), ("pop", None), ("pop", None), ("push", 3), ("peek", None)],
    [("push", 1), ("peek", None), ("push", 2), ("pop", None), ("empty", None)],
]

expected_output_suite = [
    [1, 1, False],
    [1, True],
    [-1, 1],
    [1, 2, 3],
    [1, 1, False],
]

for test_case, operations, expected_output in zip(test_cases, operations_suite, expected_output_suite):
    # Initialize the queue with the test case data
    queue = DoubleStackQueue()
    queue.stack1 = test_case[0]
    queue.stack2 = test_case[1]
    test_double_stack_queue(operations, expected_output)
