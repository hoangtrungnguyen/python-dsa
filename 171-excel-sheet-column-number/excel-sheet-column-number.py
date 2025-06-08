class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        number = 0
        for char in columnTitle:
            curr = ord(char) - ord('A') + 1
            number = number * 26
            number = number + curr
        return number