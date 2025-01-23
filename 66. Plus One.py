# Definition for a binary tree node.
from typing import Optional
from typing import List


class Solution:
    # 1. select the last index
    # 2. plus 1
    #   2.1 if = 10.
    #       is_continue = True
    #       2.1.1 loop backward. plus 1 for arr[i]:
    #       2.1.2 if number after adding > 9.
    #               if i == 0:
    #                   arr[i] = 0 and insert 1 at index = 0
    #               set is_continue = true else break.
    #
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            else:
                digits[i] = 0
        return [1] + digits


print(Solution().plusOne([1, 2, 3]))
