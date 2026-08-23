class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        seen = {0: 1}          # prefix_sum -> count of times seen
        total = 0
        result = 0
        for num in nums:
            total += num
            result += seen.get(total - k, 0)   # query BEFORE insert
            seen[total] = seen.get(total, 0) + 1
        return result