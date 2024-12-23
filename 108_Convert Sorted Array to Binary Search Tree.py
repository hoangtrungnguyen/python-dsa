from typing import Optional
from typing import List

from dsa.nodes.tree_node import TreeNode


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        """

        :param nums:
        :return:
        """
        if len(nums) == 0:
            return None

        left_node = self.sortedArrayToBST(nums[1:])

        node = TreeNode(nums[0])
        node.left = left_node
        node.right = self.sortedArrayToBST(nums[1:])
        return node



print(Solution().sortedArrayToBST([1,2,3,4,5,6,7]))
print(Solution().sortedArrayToBST([-10,-3,0,5,9]))
