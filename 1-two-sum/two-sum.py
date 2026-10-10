class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_by_number = {}
        for current_index, current_number in enumerate(nums):
            needed_number = target - current_number
            if needed_number in index_by_number:
                return [index_by_number[needed_number], current_index]
            index_by_number[current_number] = current_index