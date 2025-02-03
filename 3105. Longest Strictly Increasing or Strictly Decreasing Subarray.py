from typing import List


class Solution:

    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        max_count = 1
        n = len(nums)
        start = end = 0
        inc_count = 1

        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                inc_count += 1
            else:
                inc_count = 1
            max_count = max(inc_count, max_count)

        # print(f'max_count {max_count}')

        dec_count = 1
        for i in range(1, n):
            if nums[i] < nums[i - 1]:
                dec_count += 1
            else:
                dec_count = 1
            max_count = max(dec_count, max_count)

        # print(f'max_count {max_count}')
        return max_count

# print(f'=== actual {Solution().longestMonotonicSubarray([1,2,3,4])} - expect 4 ===')
assert Solution().longestMonotonicSubarray([1,2,3,4, 1]) == 4

# print(f'=== actual {Solution().longestMonotonicSubarray([1,2,3,4, 2])} - expect 4 ===' )
assert Solution().longestMonotonicSubarray([1,2,3,4, 2]) == 4


# print(f'=== actual  {Solution().longestMonotonicSubarray([4,3,2,0])} - expect 4 ===')
assert Solution().longestMonotonicSubarray([4,3,2,0]) == 4

# print(f'{Solution().longestMonotonicSubarray([2, 4,3,2,0])} - expect 4')
# print(f'{Solution().longestMonotonicSubarray([2, 4,3,2,0, 8])} - expect 4')
# print(f'{Solution().longestMonotonicSubarray([2])} - expect 1')
# print(f'=== actual  {Solution().longestMonotonicSubarray([2,2,2,2,])} - expect 1 ===')
# print(f'=== actual   {Solution().longestMonotonicSubarray([2,2,2,2,1])} - expect 2 ===')
assert Solution().longestMonotonicSubarray([2, 2,1,]) == 2

# print(f'{Solution().longestMonotonicSubarray([1,2,2,2,1])} - expect 2')
assert Solution().longestMonotonicSubarray([1,2,2,2,1]) == 2

# print(f'=== actual {Solution().longestMonotonicSubarray([1,2,2,2,1,2,3,4])} - expect 4 ===')
# print(f'{Solution().longestMonotonicSubarray([1,2,2,3,4 ,2,1])} - expect 3')


assert Solution().longestMonotonicSubarray([1,1,3]) == 2
