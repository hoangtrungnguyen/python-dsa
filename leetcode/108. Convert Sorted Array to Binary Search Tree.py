# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return self._diagram(self)

    def _diagram(self, treeNode, top='', root='', bottom=''):
        if treeNode is None:
            return f'{root} null\n'

        if treeNode.left is None and treeNode.right is None:
            return f'{root} {treeNode.val}\n'

        a = self._diagram(
            treeNode.right,
            f'{top} ',
            f'{top}┌──',
            f'{top}│ ',
        )

        b = f'{root}{treeNode.val}\n'

        c = self._diagram(
            treeNode.left,
            f'{bottom}│ ',
            f'{bottom}└──',
            f'{bottom} ',
        )
        return f'{a}{b}{c}'



class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) == 0:
            return None
        root = self.divide(nums, 0, len(nums) - 1)
        return root

    def divide(self, nums: List[int], start, end) -> Optional[TreeNode]:
        if start > end:
            return None
        mid = (start + end) // 2
        # print(f'start: {start}, end: {end}')
        # print(f'mid : {mid }')
        node = TreeNode(nums[mid])
        left = self.divide(nums, start, mid - 1)
        node.left = left
        right = self.divide(nums, mid + 1, end)
        node.right = right
        return node



res = Solution().sortedArrayToBST([1, 2, 3, 4, 5])
print(res)
res = Solution().sortedArrayToBST([1, 2])
print(res)
res2 = Solution().sortedArrayToBST([1, 2, 3, 4])
print(res2)
res3 = Solution().sortedArrayToBST([1])
print(res3)
res3 = Solution().sortedArrayToBST([0,1,2,3,4,5])
print(res3)



