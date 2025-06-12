from typing import List


class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        max_sum = 0
        current_sum = nums[0]
        for i in range(1, len(nums)):
            if nums[i] <= nums[i-1]:
                max_sum = max(current_sum,max_sum)
                current_sum = nums[i]
            else:
                current_sum += nums[i]
        return max(max_sum, current_sum)



print(f'{Solution().maxAscendingSum([10,20,30,5,10,50])}')
nums = [12,17,15,13,10,11,12]
print(f'{Solution().maxAscendingSum(nums)}')

