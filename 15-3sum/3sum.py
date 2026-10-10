class Solution:
    def threeSum(self, input_arr: list[int]) -> list[list[int]]:
        k = 0
        nums = sorted(input_arr)
        print(nums)
        result = []
        length = len(nums)
        while k < length - 2:
            if nums[k] > 0:
                break
            if k > 0 and nums[k] == nums[k - 1]: # duplicated target
                k += 1
                continue
            target = - nums[k]
            num_to_index = dict()
            index = k + 1
            while index < length:
                value = nums[index]
                needed_num = target - nums[index]
                # print(num_to_index)
                if needed_num in num_to_index:
                    if num_to_index[needed_num] > k :
                        while index < length - 1 and nums[index] == nums[index + 1]:
                            index += 1
                        key = [
                            nums[k], 
                            nums[num_to_index[needed_num]], 
                            nums[index]
                            ]

                        result.append(key)
                num_to_index[value] = index
                index += 1
            k += 1
        return result

        
        