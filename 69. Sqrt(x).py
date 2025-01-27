# PROBLEM
# Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.
#
# You must not use any built-in exponent function or operator.
#
# For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.

class Solution:
    # start = 0
    # end = x
    #
    # if mid * mid < x:
    #   mid = (start + end) / 2
    # else mid * mid > x:
    #   mid = (0 + mid) / 2
    def mySqrt(self, x: int) -> int:
        print(f'START: {x}')
        start, end = 0, x
        while start <= end:
        # for _ in range(0,100):
            mid = (end + start) // 2
            mid_squared = mid * mid
            if mid_squared > x:
                end = mid - 1
            elif mid_squared < x:
                start = mid + 1
            else:
                # print('END: $x\n\n')
                return mid
        return end


# print(f'final : ${Solution().mySqrt(4)}\n')
print(f'final : ${Solution().mySqrt(8)}\n')
# print(f'final : ${Solution().mySqrt(16)}\n')
# print(f'final : ${Solution().mySqrt(36)}\n')
# print(f'final : ${Solution().mySqrt(25)}\n')
# print(f'final : ${Solution().mySqrt(26)}\n')
# print(f'final : ${Solution().mySqrt(2 ** 31 - 1)}\n')



# class Solution2:
#     # x
#     # params: left, right, pointer, value
#     # 1. pointer = (left + right) / 2
#     # 2. value = pointer * pointer
#     # 3.
#     #   3.1 if value < x
#     #       pointer = (right + pointer ) / 2
#     #       right = pointer
#     #   3.2 if value > x
#     #       right = pointer
#     #       pointer = pointer / 2
#     #   3.3 vale == x
#     #       return x
#     # 4. repeat step 1
#     #
#     #
#     def mySqrt(self, x: int) -> int:
#         print(f'x: {x}')
#         left, right = 0, x
#         pointer  = (left + right) / 2
#         for _ in range(16):
#             value = pointer * pointer
#             if value < x:
#                 pointer = (right + pointer) / 2
#                 right = pointer
#             elif value > x:
#                 right = pointer
#                 pointer = pointer / 2
#             else:
#                 return pointer
#
#
#         print(f'pointer {pointer}, right: {right}')
#         return pointer
#


# print(f'final : ${Solution().mySqrt(4)}\n')
# print(f'final : ${Solution().mySqrt(16)}\n')
# print(f'final : ${Solution().mySqrt(36)}\n')
# print(f'final : ${Solution().mySqrt(25)}\n')
# print(f'final : ${Solution().mySqrt(2 ** 31 - 1)}\n')


# START: 4
# final : $2.0
#
# START: 16
# final : $4.0
#
# START: 36
# final : $6.0
#
# START: 25
# final : $5.0
#
# START: 2147483647
# final : $46340.950001051984
# print(f'final : ${Solution2().mySqrt(4)}\n')
# print(f'final : ${Solution2().mySqrt(16)}\n')
# print(f'final : ${Solution2().mySqrt(36)}\n')
# print(f'final : ${Solution2().mySqrt(25)}\n')
# print(f'final : ${Solution2().mySqrt(2 ** 31 - 1)}\n')

