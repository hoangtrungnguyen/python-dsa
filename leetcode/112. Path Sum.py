# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # Depth First Traverse to leaf
    # 1. At each level: targetSum - node.value
    # 2. At leaf: if targetSum == 0 return True
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False
        if targetSum < 0:
            return False
        targetSum -= root.val
        if targetSum == 0 and root.left is None and root.right is None:
            return True

        return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)


# Level 0: Root node
root = TreeNode(5)

# Level 1: Children of the root
root.left = TreeNode(4)
root.right = TreeNode(8)

# Level 2: Children of level 1 nodes
root.left.left = TreeNode(11)
root.left.right = TreeNode(13)
root.right.right = TreeNode(4)  # Note: 8 only has a right child

# Level 3: Children of level 2 nodes
root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(2)
root.right.right.right = TreeNode(1)  # Note: 4 only has a right child

print(f'expect True: {Solution().hasPathSum(root, 22)}')

# Level 0: Root node
root = TreeNode(1)

# Level 1: Children of the root
root.left = TreeNode(2)
root.right = TreeNode(3)
print(f'expect False: {Solution().hasPathSum(root, 5)}')

# Level 0: Root node
root = TreeNode(1)
print(f'expect True: {Solution().hasPathSum(root, 1)}')

root = TreeNode(2)
print(f'expect False: {Solution().hasPathSum(root, 1)}')
