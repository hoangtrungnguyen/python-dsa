# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0
        
        def get_left_height(node):
            count = 0
            while node:
                count += 1
                node = node.left
            return count
        
        def get_right_height(node):
            count = 0
            while node:
                count += 1
                node = node.right
            return count
        


        lh = get_left_height(root)
        rh = get_right_height(root)

        # If left and right heights are
        # equal return 2^height(1<<height) -1
        if lh == rh:
            return ( 1 << lh ) - 1
        
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
