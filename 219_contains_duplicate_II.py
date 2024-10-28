from typing import Optional
from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        """
        The window: start from i and end at j
        A map: int_to_index (We're finding nums[i] == nums[j] so we need a map int to index)

        int start
        for end in range:
            num = nums[end]
            if num in int_to_index and abs(int_to_index[num] - end) <= k:
                return true
            int_to_index[num] = end


        :param nums:
        :param k:
        :return:
        """
        int_to_index = {}
        for end, num in enumerate(nums):
            if num in int_to_index and end - int_to_index[num] <= k:
                return True
            int_to_index[num] = end
        return False


# print(Solution().containsNearbyDuplicate(nums=[1, 2, 3, 1], k=3))
# # true
# print(Solution().containsNearbyDuplicate(nums=[1,2,3,1,2,3], k=2))
# # false
# print(Solution().containsNearbyDuplicate(nums=[1,0,1,1], k=1))
# # true
# print(Solution().containsNearbyDuplicate(nums=[1], k=1))
# # false
# print(Solution().containsNearbyDuplicate(nums=[1, 1], k=1))
# # true
print(Solution().containsNearbyDuplicate(nums=[1,3,4,2, 1], k=1))
# false
