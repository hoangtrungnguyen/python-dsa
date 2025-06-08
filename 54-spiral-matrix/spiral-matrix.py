class Cell:
    def __init__(self, x, y, direction: int):
        self.x = x
        self.y = y
        self.direction = direction


    def move(self):
        # 0 -> right
        # 1 -> bottom
        # 2 -> left
        # 3 -> top

        if self.direction == 0:
            self.y = self.y + 1
        elif self.direction == 1:
            self.x = self.x + 1
        elif self.direction == 2:
            self.y = self.y - 1
        elif self.direction == 3:
            self.x = self.x - 1 
        else:
            print("can't find direction")

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        '''
        action = [right, bottom, left, up]
        '''
        row_length = len(matrix[0])
        column_length = len(matrix)
        filled_matrix = [ [0 for j in range(len(matrix[i]))] for i in range(len(matrix))]

        def is_right_valid(i:int, j:int):
            # boundary
            if j + 1 >= row_length:
                return False
            
            if filled_matrix[i][j + 1] != 0:
                return False

            return True
        
        def is_bottom_valid(i:int, j:int):
            # boundary
            if i + 1 >= column_length:
                return False
            
            if filled_matrix[i + 1][j] != 0:
                return False

            return True

        def is_left_valid(i:int, j:int):
            # boundary
            if j - 1 < 0:
                return False
            
            if filled_matrix[i][j - 1] != 0:
                return False

            return True

        def is_top_valid(i:int, j:int):
            # boundary
            if i - 1 < 0:
                return False
            
            if filled_matrix[i - 1][j] != 0:
                return False

            return True
        
        # def select_direction(current_direction:int):
        direction_to_validation  = {
            0: is_right_valid,
            1: is_bottom_valid,
            2: is_left_valid,
            3: is_top_valid
        }

        # print(direction_to_validation[0](0,0))
          
        curr = Cell(0,0,0)
        result = []
        
        # 0 -> right
        # 1 -> bottom
        # 2 -> left
        # 3 -> top
        
        while curr != None:
            filled_matrix[curr.x][curr.y] = 1
            # print("---")
            # print(filled_matrix)
            result.append(matrix[curr.x][curr.y])
            # prioritize direction
            # validate from current direction with clock direction
            current_direction = curr.direction % 4
            if direction_to_validation[current_direction % 4](curr.x, curr.y):
                curr.direction = current_direction % 4
            elif direction_to_validation[(current_direction + 1) % 4 ](curr.x, curr.y):
                curr.direction = (current_direction + 1) % 4
            elif direction_to_validation[(current_direction + 2) % 4 ](curr.x, curr.y):
                curr.direction = (current_direction + 2) % 4
            elif direction_to_validation[(current_direction + 3) % 4 ](curr.x, curr.y):
                curr.direction = (current_direction + 3) % 4
            else:
                curr = None     
                break
            curr.move()

        return result

