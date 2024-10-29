from typing import Optional
from typing import List


class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        """
        sorting ?

        :param nums:
        :param indexDiff:
        :param valueDiff:
        :return:
        """
        int_to_index = {}

        for end, num in enumerate(nums):
            if num in int_to_index and end != int_to_index[num] and end - int_to_index[num] <= indexDiff and abs(
                    num - nums[int_to_index[num]]) <= valueDiff:
                return True
            int_to_index[num] = end
        return False


print(Solution().containsNearbyAlmostDuplicate([1, 2, 3, 1], 3, 0)) # true
print(Solution().containsNearbyAlmostDuplicate([1, 5, 9, 1, 5, 9], 2, 3)) # false
print(Solution().containsNearbyAlmostDuplicate([1, 1], 1, 0))  # true
print(Solution().containsNearbyAlmostDuplicate([2, 2], 3, 1))  # false
print(Solution().containsNearbyAlmostDuplicate([8,7,15,1,6,1,9,15], 1, 3))  # false


