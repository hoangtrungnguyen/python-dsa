class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        group_count = [0] * k          # was: list()  -> IndexError on any access
        sorted_nums = sorted(nums)
        print(f'sorted_numes {sorted_nums}')
        key_count = [0] * k
        i = 0
        count = 0
        l = len(sorted_nums)
        while i < l:
            if i < l - 1 and sorted_nums[i] == sorted_nums[i+1]:
                count += 1
            else:
                count += 1
                if count > group_count[-1]:
                    j = len(group_count) - 1
                    while j > 0 and count > group_count[j-1]:   
                        group_count[j] = group_count[j-1]
                        key_count[j] = key_count[j-1]
                        j -= 1
                    group_count[j] = count
                    key_count[j] = sorted_nums[i]
                count = 0
            i += 1
        return key_count