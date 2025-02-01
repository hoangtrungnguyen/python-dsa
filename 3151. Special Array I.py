from typing import List


class Solution:
    # Ideas: Using sliding window
    # 1. window_size = 2
    # 2. if (1st element is odd and 2nd is even) or (1st element is even and 2nd is odd):
    #   2.1 TRUE : move to window size 1 step to the right
    #   2.1 FALSE: return false
    # 3. repeat step 2
    def isArraySpecial(self, nums: List[int]) -> bool:
        window_size = 2
        for i in range(0,len(nums)-1):
            # print(f'i {i}')
            first = nums[i]
            second = nums[i + 1]
            # print(f'first {first}, second {second}')
            if (first % 2 == 0 and second % 2 == 1) or (first % 2 == 1 and second % 2 == 0):
                continue
            else:
                return False

        return True


print(Solution().isArraySpecial(nums=[2, 1, 4]))
print(Solution().isArraySpecial(nums=[2, 1, 4, 3]))
print(Solution().isArraySpecial(nums=[2, 1, 4, 8]))
print(Solution().isArraySpecial(nums=[2, 1, 1]))
print(Solution().isArraySpecial(nums=[2]))
