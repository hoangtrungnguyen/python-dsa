class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        '''
        action = [right, bottom, left, up]
        '''
        num_of_row = len(matrix)
        num_of_col = len(matrix[0])

        top_row, bottom_row = 0, num_of_row - 1
        left_col, right_col = 0, num_of_col - 1

        # use filled matrix to check
        # filled_matrix = [ [0 for j in range(len(matrix[i]))] for i in range(len(matrix))]
        result = []


        while top_row <= bottom_row and left_col <= right_col:
            for col in range(left_col, right_col + 1):
                # filled_matrix[top_row][col] += 1
                result.append(matrix[top_row][col])
            top_row += 1 
            for row in range(top_row, bottom_row + 1):
                # filled_matrix[row][right_col] += 1
                result.append(matrix[row][right_col])
            right_col -= 1

            # print(f'bottom_row {bottom_row}')
            if top_row <= bottom_row:
                for col in range(right_col, left_col - 1, -1):
                    # print(f'col {col}')
                    # filled_matrix[bottom_row][col] += 1    
                    result.append(matrix[bottom_row][col])
                bottom_row -= 1
            # range will be stop before (exclusive) the value we put in. Therefore, we will have to minus 1
            # symbol [, )
            if left_col <= right_col:
                for row in range(bottom_row, top_row - 1, -1):
                    # filled_matrix[row][left_col] += 1
                    result.append(matrix[row][left_col])                
                left_col += 1


        # print(filled_matrix)
        return result
