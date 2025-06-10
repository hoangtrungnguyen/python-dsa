class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Handle empty or short lists
        if len(heights) <= 1:
            return 0

        start = 0
        end = len(heights) - 1

        max_area = 0
        while end > start:
            height = min(heights[start], heights[end])
            width = end - start
            area = height * width
            max_area = max(area, max_area)

            if heights[start] < heights[end]:
                start += 1
            else:
                end -= 1
        
        return max_area

        
# Example usage:
solver = Solution()
heights1 = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(f"Result for {heights1}: {solver.maxArea(heights1)}") # Output: 49, Correct for this case

heights2 = [1, 2, 4, 3]
print(f"Result for {heights2}: {solver.maxArea(heights2)}") # Output: 4, Incorrect. Correct is 6 (between 2 and 3)
