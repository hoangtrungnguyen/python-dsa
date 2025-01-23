# Definition for a binary tree node.
from typing import Optional
from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):  # Define how you want to print the object
        return f"Node:{self.val}"

## Attempt 1
class Solution:
    '''
    push the root into the queue
    for each node in the level:
        we store all children into a queue
            now we have all element
    then push node into queue
    '''

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = [root]
        result = []

        while queue:
            level_size = len(queue)
            level_elements = []
            for _ in range(level_size):
                node: TreeNode = queue.pop(0)
                level_elements.insert(0, node.val)
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)

            result.append(level_elements)


        return result
#
#     # def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
#     #     queue = [root]
#     #     elements = []
#     #     level_elements = []
#     #     print('{}', root.val)
#     #     # levelOrder(root.left)
#     #     result = [[root.val]]
#     #     depth = 1
#     #     while True:
#     #         if len(queue) == 0:
#     #             break
#     #         node = queue.pop(0)
#     #         if node is None:
#     #             break
#     #         level_elements.append( node.val)
#     #         elements.append(node.val)
#     #
#     #         if len(result) > 0:
#     #             last = result[len(result)-1]
#     #             print('len(last)', len(last))
#     #             # if(level_elements)
#     #             result.append(level_elements)
#     #             level_elements = []
#     #             # if len(queue) == 0:
#     #             #     result.append(level_elements)
#     #             #
#     #
#     #         if node.left is not None:
#     #             queue.insert(0, node.left)
#     #         if node.right is not None:
#     #             queue.insert(0, node.right)
#     #             # level_elements.insert(0, node.right.val)
#     #
#     #         print('queue:')
#     #
#     #         print(*queue, sep=" - ")
#     #     print('elements ', elements)
#     #     print('Result', result)
#     #     return result
#
#     #
#     # def breadFirstSearch(self,  root: Optional[TreeNode], queue: List[TreeNode] ):


# Attempt 2
# class Solution:
#     '''
#     1. for each level add all node into a queue
#     2. for each node in the queue add its value into a list
#     3. after loop through all the node in the queue, add children of each node into the queue
#     4. repeat 1, 2, 3 until the queue is empty
#     '''
#     def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
#         queue = []
#
#
#         while True:
#
#
#         return visited






def list_to_tree(lst):
    """
    Converts a list representation of a binary tree to a TreeNode object.

    Args:
        lst: A list representing the binary tree in level order traversal.
             'null' indicates an empty node.

    Returns:
        The root of the constructed binary tree.
    """
    if not lst:
        return None

    root = TreeNode(lst[0])
    queue = [root]
    i = 1

    while queue and i < len(lst):
        curr_node = queue.pop(0)

        if lst[i] != 'null':
            curr_node.left = TreeNode(lst[i])
            queue.append(curr_node.left)
        i += 1

        if i < len(lst) and lst[i] != 'null':
            curr_node.right = TreeNode(lst[i])
            queue.append(curr_node.right)
        i += 1

    return root

# Example usage:
# input_list = [3, 9, 20, 'null', 'null', 15, 7]
# root = list_to_tree(input_list)

# (Optional) Print the tree in level order to verify
def print_tree(root, indent="", last=True):
    """
    Prints the tree structure in a visually appealing way.

    Args:
        root: The root of the tree.
        indent: The current indentation string.
        last: True if the node is the last child of its parent.
    """
    if root is None:
        return

    print(indent, end="")
    if last:
        print("└─", end="")
        indent += "  "
    else:
        print("├─", end="")
        indent += "| "

    print(root.val)

    print_tree(root.left, indent, False)
    print_tree(root.right, indent, True)



# Example usage:
print('case 1')
input_list = [3, 9, 20, 'null', 'null', 15, 7]
root = list_to_tree(input_list)
print_tree(root)
print(Solution().levelOrder(root))

print('case 2')
input_list = [1,2,'null', 'null' ,3,4,5,6,7,8,9]
root = list_to_tree(input_list)
print_tree(root)

print(Solution().levelOrder(root))