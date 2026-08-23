import string

class Solution:
    def isPalindrome(self, s: str) -> bool:
        word =s 
        i = 0
        j = len(word) - 1

        while i < j:

            if ord(word[i].lower()) not in range(97, 123) and ord(word[i].lower()) not in range(48, 58):
                i += 1
            elif ord(word[j].lower()) not in range(97, 123) and ord(word[j].lower()) not in range(48, 58):
                j -= 1
            elif ord(word[i].lower()) != ord(word[j].lower()):
                return False
            else:
                i += 1
                j -= 1
        return True
        