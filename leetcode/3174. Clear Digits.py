class Solution:
    """
    stack
    for char in s backward order
    """
    def clearDigits(self, s: str) -> str:
        stack = []
        chars = list(s)
        # chars.reverse()
        for e in chars:
            # print(f' {e} - {e.isdigit()} ')
            if len(stack) >= 1 and e.isdigit():
                stack.pop()
            else:
                stack.append(e)

        return "".join(stack)


print(f"{Solution().clearDigits('abc')}")
print(f"{Solution().clearDigits('cb34')}")


stack = []

stack.append(1)
stack.append(2)
print(stack)
stack.pop()
print(stack)