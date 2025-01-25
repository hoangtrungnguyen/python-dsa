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
        start = 0
        end = x
        # while start <= end:
        for _ in range(0,100):
            mid = (end + start) / 2
            if mid * mid > x:
                end = mid
            elif mid * mid < x:
                start = mid
            else:
                print('END: $x\n\n')
                return mid
            print(f"mid {mid}")
            print(f"mid*mid {mid * mid}")
            print(f"start {start}")
            print(f"end {end}")
            print('-'*10)
        # start = 0
        # end = x
        # mid = (start + end) // 2
        print(f'END: {x}\n\n')
        return ((end + start) / 2) // 1


# print(f'final : ${Solution().mySqrt(4)}\n')
# print(f'final : ${Solution().mySqrt(16)}\n')
# print(f'final : ${Solution().mySqrt(36)}\n')
# print(f'final : ${Solution().mySqrt(25)}\n')
print(f'final : ${Solution().mySqrt(2 ** 31 - 1)}\n')
