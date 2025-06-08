class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = 0
        element = None
        for num in nums:
            if counter == 0:
                element = num
                counter = 1
            elif num == element:
                counter += 1
            else:
                counter -= 1
        return element