from typing import Optional
from typing import List


class Solution:
    # Simple self-explanation:
    #    after all subtractions on each element will the array is a strictly increasing array ?
    # inputs
    #   - array (element in array is greater than zero)
    # variables
    #   - visited_indexes
    #   - prime_nums
    # functions
    #   - detect if a number is a prime number
    #   -
    # algorithm
    #   1.

    def primeSubOperation(self, nums: List[int]) -> bool:
        print(f'origin {nums}')

        end = len(nums) - 1
        while end > 0 and nums[end] > nums[end - 1]:
            end -= 1
        # print(f'end {end}')
        for i in range(0, end, 1):
            print(f'---- round {i} ----')
            # set nums[i] = smallest when subtract to a prime
            # increase by i by 1
            # set nums[i] = 1 level bigger than nums[i-1]
            #

            e = nums[i]
            print(f'e {e}')
            p = self.findNearestPrime(e)
            print(f'p {p}')
            subtract = e - p

            print(f'subtract {subtract}')
            print(f'nums: {nums}')
            while i > 0 and subtract <= nums[i - 1]:
                print(f'subtract {subtract}')
                e -= 1
                p = self.findNearestPrime(e)
                # if p == 0 and subtract <= nums[i - 1]:
                #     return False
                # before_subtract = nums[i]
                subtract = nums[i] - p
                print(f'nums[i-1] {nums[i - 1]}')
                print(f'nums[i] {nums[i]}')
                # if p == 0 and subtract == 5:
                #     return False
                # if p == 0 and subtract == 1:
                #     return False

                if self.is_prime(nums[i - 1]) and (self.is_prime(nums[i]) or nums[i] == 1) and nums[i] < nums[i - 1]:
                    return False
                if nums[i] <= nums[i - 1]:
                    return False
                print(f'p {p}')

            nums[i] = subtract
            print('--- end round ---')


        print(f'end:{end}')
        print(f'nums: {nums}')
        if end > 0 and nums[end - 1] >= nums[end]:
            return False

        return True

    def is_prime(self, n: int):
        """
        Checks if a number is prime.

        Args:
          n: The number to check.

        Returns:
          True if n is a prime number, False otherwise.
        """
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def findNearestPrime(self, num: int) -> int:
        if num < 2:
            return 0

        for i in range(num - 1, -1, -1):
            is_prime = self.is_prime(i)
            if is_prime:
                return i
        return 0


#
#
# #
# # expect [2, 3, 5, 7, 11, 19]
# print(primes)
# #
# nearest_prime = Solution().binarySearchNearest(14, primes)
# print(f'nearest_prime {nearest_prime}')
# assert nearest_prime == 13, f'input: 14 -> expect: 13. actual {nearest_prime}'
# print(nearest_prime)
# #
# # nearest_prime = Solution().binarySearchNearest(7, primes)
# # print('input: 7 -> expect 5')
# # print(nearest_prime)
# #
# #
# nearest_prime = Solution().binarySearchNearest(2, primes)
# assert nearest_prime == 0, f'input: 2 -> expect 0. actual {nearest_prime}'
# print(nearest_prime)
#
# # nearest_prime = Solution().binarySearchNearest(1, primes)
# # print('input: 1 -> expect 0')
# # print(nearest_prime)
# #
# #
#
#
nearest_prime = Solution().findNearestPrime(20)
print('input: 20 -> expect 19')
assert nearest_prime == 19, f'input: 20 -> expect: 19. actual {nearest_prime}'
print(nearest_prime)

nearest_prime = Solution().findNearestPrime(94)
assert nearest_prime == 89, f'input: 94  -> expect: 89. actual {nearest_prime}'
print(nearest_prime)
#
# nearest_prime = Solution().binarySearchNearest(18, primes)
# print('input: 18 -> expect 17')
# assert nearest_prime == 17, f'input: 18 -> expect 17. actual: {nearest_prime}'
# print(nearest_prime)

# nearest_prime = Solution().binarySearchNearest(5, primes)
# assert nearest_prime == 3, f'input: 5 -> expect 3. actual: {nearest_prime}'
# print(nearest_prime)

# nearest_prime = Solution().findNearestPrime(5, [0, 2, 3, 5, 7, 11])
# assert nearest_prime == 3, f'input: 5 -> expect 3. actual: {nearest_prime}'

#
output = Solution().primeSubOperation([4,9,6,10])
assert output == True
#
output = Solution().primeSubOperation([6,8,11,12])
assert output == True


output = Solution().primeSubOperation([5,8,3])
assert output == False


output = Solution().primeSubOperation([5])
assert output == True

output = Solution().primeSubOperation([15,20,17,7,16])
assert output == True

output = Solution().primeSubOperation([17, 20, 5, 15, 6])
assert output == False

output = Solution().primeSubOperation([18,12,14,6])
assert output == False
output = Solution().primeSubOperation([5,13,4,13])
assert output == False

output = Solution().primeSubOperation([98, 21, 9, 53, 72, 13, 94, 81, 68, 67])
assert output == True

output = Solution().primeSubOperation([6, 6, 1, 20, 10])
assert output == False

output = Solution().primeSubOperation([2,2,8,20,2])
assert output == False

