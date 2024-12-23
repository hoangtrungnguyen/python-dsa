from typing import Optional
from typing import List

from dsa.nodes.tree_node import TreeNode


# Hint: Use one and zero as an indicator for height of the tree
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        # If a non-leaf node is missing a child, it's not balanced
        # if (root.left is None and root.right is not None) or \
        #         (root.left is not None and root.right is None):
        #     return False
        gap = abs(self.height(root.left) - self.height(root.right)) <= 1
        left_balanced = self.isBalanced(root.left)
        right_balanced = self.isBalanced(root.right)
        return (gap and
                left_balanced and right_balanced)

    def height(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        return max(self.height(root.left) , self.height(root.right)) + 1


from dsa.nodes.tree_node import array_to_tree
print('--- START: root -1---')
root0 = array_to_tree([3, 9, None])
print(root0)
print(Solution().isBalanced(root0))
print('--- END: root -1---')
print('--- START: root 0---')
root0 = array_to_tree([3, 9, 3, None, None, 2, 1, None, None, None, 12])
print(root0)
print(Solution().isBalanced(root0))
print('--- END: root 0---')
#
print('--- START: root1 ---')
root1 = array_to_tree([3, 9, 20, None, None, 15, 7])
print(root1)

print(Solution().isBalanced(root1))
print('--- END: root1 ---')

print('--- START: root2 ---')
root2 = array_to_tree([1, 2, 2, 3, 3, None, None, 4, 4])
print(root2)
print(Solution().isBalanced(root2))

print('--- END: root2 ---')
print('--- START: root3 ---')
root3 = array_to_tree([])
print(Solution().isBalanced(root3))
print(root3)
print('--- END: root3 ---')
print('--- END: root4 ---')
root4 = array_to_tree([1,2,2,3,None,None,3,4,None,None,4])
print(root4)
print(f'actual: {Solution().isBalanced(root4)}')
print('--- END: root4 ---')
# root4 = array_to_tree([1,2 ])
# print('expect: True')
# print(root4)
# print(f'actual: {Solution().isBalanced(root4)}')
# print('--- END: root5 ---')
#
# root = array_to_tree([1,2,3,4,5,6, None ])
# print('expect: True')
# print(root)
# print(f'actual: {Solution().isBalanced(root)}')
# print('--- END: root6 ---')
#
# print('--- START: root 7---')
# root = array_to_tree([1,2,3,4,5,6,None,8])
# print('expect: True')
# print(root)
# print(f'actual: {Solution().isBalanced(root)}')
# print('--- END: root 7 ---')
