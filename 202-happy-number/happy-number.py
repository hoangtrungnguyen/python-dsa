class Solution:
    def _get_next_number(self, number: int) -> int:
        """
        Helper function to calculate the sum of the squares of the digits of a number.
        Example: _get_next_number(19) returns 1^2 + 9^2 = 1 + 81 = 82.
        """
        output = 0
        while number > 0:  # Iterate while there are digits left
            digit = number % 10  # Get the last digit
            output += digit * digit  # Add the square of the digit to the output
            number //= 10  # Remove the last digit
        return output

    def isHappy(self, n: int) -> bool:
        """
        Determines if a number n is a happy number using Floyd's Cycle Detection algorithm.

        A happy number is a number which eventually reaches 1 when replaced by
        the sum of the square of its digits repeatedly. If the process results in a cycle
        that does not include 1, the number is not happy.

        Args:
            n: A positive integer.

        Returns:
            True if n is a happy number, False otherwise.
        """
        if n <= 0: # Happy numbers are typically defined for positive integers.
            return False # Or raise an error, depending on expected constraints.
        if n == 1: # 1 is a happy number.
             return True

        slow = n  # The "tortoise" pointer
        fast = n  # The "hare" pointer

        # The loop continues until a cycle is detected or 1 is reached.
        # This structure is akin to a do-while loop, ensuring at least one iteration.
        while True:
            slow = self._get_next_number(slow)  # Move slow pointer one step
            
            # Move fast pointer two steps
            fast = self._get_next_number(fast) 
            fast = self._get_next_number(fast) 

            if fast == 1:
                # If the fast pointer reaches 1, the number is happy.
                # (The slow pointer will also eventually reach 1).
                return True
            
            if slow == fast:
                # If the pointers meet, a cycle has been detected.
                # Since 'fast == 1' was checked just before this,
                # if they meet here, it means they are in a cycle that does not include 1.
                # Therefore, the number is not happy.
                return False