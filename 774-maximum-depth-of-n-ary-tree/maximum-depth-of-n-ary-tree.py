"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:

    def maxDepth(self, root: 'Node') -> int:
        if root is None:
            return 0
        return self.findDepth(root) + 1

    def findDepth(self, root: 'Node') -> int:
        if root is None:
            return 0
        list_branch_depth = []
        for node in root.children:
            branch_depth = self.findDepth(node) + 1
            list_branch_depth.append(branch_depth)
        
        if list_branch_depth:
            return max(list_branch_depth)
        else:
            return 0