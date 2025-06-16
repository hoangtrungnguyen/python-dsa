class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        S = ((n + 1) * n) / 2
        return int(S - sum(nums))
        