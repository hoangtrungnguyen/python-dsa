class Solution:
    # i = 1
    # while i <= 2
    #   array = array with length i
    #   
    #   
    def generate(self, numRows: int) -> List[List[int]]:
        # Constraint: 1 <= numRows <= 30
        # If numRows could be 0, we'd handle it:
        # if numRows == 0:
        #     return []

        triangle: List[List[int]] = []

        for i in range(numRows):
            # `i` is the 0-based row index.
            # Row `i` has `i + 1` elements.
            num_elements_in_current_row = i + 1

            if i == 0:
                # The first row is always [1]
                current_row = [1]
            else:
                # Get the previous row from the triangle
                prev_row = triangle[i - 1] # Or triangle[-1]
                
                # Construct the current row using a list comprehension.
                # `k` is the 0-based element index within the current_row.
                # It ranges from 0 to `num_elements_in_current_row - 1` (which is `i`).
                current_row = [
                    1 if k == 0 or k == i  # Elements at the ends of the row are 1
                    else prev_row[k - 1] + prev_row[k]  # Inner elements are sum of two above
                    for k in range(num_elements_in_current_row) # Iterate for each element in the current row
                ]
            
            triangle.append(current_row)
            
        return triangle