class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = ''
        # phần dư
        carry = 0
        length = max(len(a), len(b))
        binary2 = b.rjust(length,  "0")
        binary1 = a.rjust(length,  "0")
        for i in range(length - 1 ,-1, -1):
            # print('i  {}'.format(i))
            bit1 = int(binary1[i])
            bit2 = int(binary2[i])
            sum = bit1 + bit2 + carry
            carry = sum // 2
            result = sum % 2
            res = str(result) + res
        if carry > 0:
            res = str(carry) + res
        return res


print(Solution().addBinary("101", "1011"))
