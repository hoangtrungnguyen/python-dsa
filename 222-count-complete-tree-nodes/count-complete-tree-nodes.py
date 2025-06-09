# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        # if root.left is None and root.right is None:
        #     return 1
        def dfs(node: Optional[TreeNode], count: int) -> int:
            if node is None:
                return 0
            count = dfs(node.left, count) + dfs(node.right, count) + 1 
            return count 

        return dfs(root, 0)
        # return count