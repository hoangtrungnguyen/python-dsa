from typing import List


class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        count = 0  # Count of pairs where nums[i] > nums[i+1]

        for i in range(n):
            if nums[i] > nums[(i + 1) % n]:  # Compare with next, wrapping around
                count += 1

        return count <= 1  # Rotated sorted array has at most one such pair



print(f'{Solution().check([3,4,5,1,2])} - expect: True')
print(f'{Solution().check([2,1,3,4])} - expect: False')
print(f'{Solution().check([4])} - expect: True')
print(f'{Solution().check([3,4])} - expect: True')
