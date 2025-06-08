class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = {}
        for num in nums:
            if num not in counter:
                counter[num] = 1
            else:
                counter[num] = counter[num] + 1

        length = len(nums)
        for key, val in counter.items():
            if val > length / 2:
                return key
        return -1