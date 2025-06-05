# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        list_of_node = []
        self.helper(root, list_of_node)
        return list_of_node

    def helper(self, curr: Optional[TreeNode], list_of_node: List[int]):
        if curr is None:
            return
        self.helper(curr.left, list_of_node)
        self.helper(curr.right, list_of_node)
        list_of_node.append(curr.val)        
