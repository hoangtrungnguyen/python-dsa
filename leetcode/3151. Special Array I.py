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

class Solution2:
    def isArraySpecial(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 1:
            return True
        prev = nums[0] & 1
        for i in range(1, n):
            next = nums[i] & 1
            if prev ^ next == 0: #XOR operator
                return False
            prev = next
        return True



# print(Solution().isArraySpecial(nums=[2, 1, 4]))
# print(Solution().isArraySpecial(nums=[2, 1, 4, 3]))
# print(Solution().isArraySpecial(nums=[2, 1, 4, 8]))
# print(Solution().isArraySpecial(nums=[2, 1, 1]))
# print(Solution().isArraySpecial(nums=[2]))
print(Solution2().isArraySpecial(nums=[2, 1, 4]))
print(Solution2().isArraySpecial(nums=[2, 1, 4, 8]))
