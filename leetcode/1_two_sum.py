from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        remain_to_index = {}
        for i in range(len(nums)):
            remain = target - nums[i]
            if nums[i] in remain_to_index:
                return [remain_to_index.get(nums[i]), i]
            else:
                remain_to_index.setdefault(remain, i)
        return []

case1 = Solution().twoSum([2,7,11,15], 9)
assert case1 == [0,1]

case2 = Solution().twoSum([2,123,4,2,123, 323, 1, 7], 9)
assert case2 == [0,7]


case3 = Solution().twoSum([2,7], 9)
assert case3 == [0,1]

case4 = Solution().twoSum([2,7,11,15], 9)
assert case4 == [0,1]
case5 = Solution().twoSum([1, 3,2, 7], 9)
assert case5== [2,3]


