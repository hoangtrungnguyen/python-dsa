from typing import Optional
from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums)
        mid = (start + end) // 2
        while start < end and nums[mid] != target:
            if nums[mid] < target:
                start = mid + 1
            elif nums[mid] > target:
                end = mid
            mid = (start + end) // 2
        return mid


print(Solution().searchInsert([3,5,6], 5)) # 1
print(Solution().searchInsert([3,5], 7)) # 2
print(Solution().searchInsert( [1,3,5,6], 2)) # 1
print(Solution().searchInsert( [1,3,5,6], 7)) # 4
print(Solution().searchInsert( [1], 7)) # 1

