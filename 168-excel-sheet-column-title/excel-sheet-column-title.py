class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        if columnNumber <= 0:
            return ""
        SIZE = 26
        number = columnNumber
        result_chars = []
        while number > 0:
            remainder = (number - 1) % SIZE
            quotient = (number - 1) // SIZE
            print(quotient)
            result_chars.insert(0, chr(65 + remainder))
            number =  quotient
        
        return "".join(result_chars)
            