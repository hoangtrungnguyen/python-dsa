class Solution:
    # args: valid parentheses string: s
    # strs = []
    # stack
    # temp
    # for char in s:
    #   if char is (:
    #       push ( to stack
    #       temp += (
    #   else:
    #       pop from stack
    #       temp += )
    #   if stack is empty
    #       strs += (temp.remove(len(temp) and temp.remove(0))
    #
    # return strs.join('')
    #
    #
    # def removeOuterParentheses(self, s: str) -> str:
    #     strs = []
    #     stack = []
    #     temp = ''
    #     for char in s:
    #         # print(f'char: {char}')
    #         if char == '(':
    #             stack.append(char)
    #             temp += char
    #         else:
    #             temp += char
    #             stack.pop()
    #             if len(stack) == 0:
    #                 # print(temp)
    #                 strs.append(temp[1:len(temp) - 1])
    #                 temp = ''
    #         # print(f'temp: {temp}')
    #         # print(f'stack: {stack}')
    #     # print(f'str: {strs}')
    #     return ''.join(strs)
    def removeOuterParentheses(self, s: str) -> str:
        strs = []
        counter = 0
        start = 0
        for i in range(len(s)):
            if s[i] == '(':
                counter += 1
            else:
                counter -= 1
                if counter == 0:
                    strs.append(s[start + 1:i])
                    start = i + 1
        return ''.join(strs)


# ()()()
# ()()()()(())
#
print(Solution().removeOuterParentheses('(()())(())'))
print(Solution().removeOuterParentheses('(()())(())(()(()))'))
print(Solution().removeOuterParentheses('()()'))
