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
            
            # pointer to higher remain
            if heights[start] < heights[end]:
                start += 1
            else:
                end -= 1
        
        return max_area
