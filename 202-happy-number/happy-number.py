class Solution:
    def isHappy(self, n: int) -> bool:
        def get_next_number(n):    
            output = 0
            while n:
                digit = n % 10
                output += digit ** 2
                n = n // 10
            return output

        slow = get_next_number(n)
        fast = get_next_number(get_next_number(n))
        if fast == 1:
            return True
        while fast != slow:
            slow = get_next_number(slow)
            fast = get_next_number(get_next_number(fast))

            if fast == 1:
                return True
        
        return False