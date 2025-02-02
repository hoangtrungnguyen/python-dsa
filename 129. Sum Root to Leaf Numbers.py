# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        return self.DFS(root, 0)

    def DFS(self, node: Optional[TreeNode], num: int) -> int:
        if not node:
            return 0
        num = num * 10 + node.val

        if node.left is None and not node.right:
            return num

        left_num = self.DFS(node.left, num)
        right_num = self.DFS(node.right, num)
        return left_num + right_num



root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

print(f'actual {Solution().sumNumbers(root)} - expected: 25')


root = TreeNode(4)
node9 = TreeNode(9)
root.left = node9
node9.left = TreeNode(5)
node9.right =  TreeNode(1)
root.right = TreeNode(0)

print(f'actual {Solution().sumNumbers(root)} - expected: 1026')

root = TreeNode(4)
print(f'actual {Solution().sumNumbers(root)} - expected: 4')
