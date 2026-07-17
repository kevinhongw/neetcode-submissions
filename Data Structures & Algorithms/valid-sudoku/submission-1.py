class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check row
        for row in range(9):
            seen = set()
            for i in range(9):
                if board[row][i] == '.':
                    continue
                if board[row][i] in seen:
                    return False

                seen.add(board[row][i])

        # check column
        for column in range(9):
            seen = set()
            for i in range(9):
                if board[i][column] == '.':
                    continue
                if board[i][column] in seen:
                    return False

                seen.add(board[i][column])

        # check 3x3
        for square in range(9): # nine boxes
            seen = set()
            for row_i in range(3):
                for column_i in range(3):
                    row = (square // 3) * 3 + row_i
                    column = (square % 3) * 3 + column_i

                    if board[row][column] == '.':
                        continue
                    if board[row][column] in seen:
                        return False
                    seen.add(board[row][column])
        
        return True


#
#  0 1 2
#  3 4 5
#  6 7 8
#
# row will always be n // 3 * 3 + row_i
# column will be n % 3 * 3 + column_i


# 0 -> 0,0 0,1 0,2  1,0 1,1 1,2  2,0 2,1 2,2
# 1 -> 0,3 0,4 0,5  1,3 1,4 1,5  2,3 2,4 2,5 
# 2 -> 0,6 0,7 0,8  1,6 1,7 1,8  2,6 2,7 2,8

# 3 -> 3,0 3,1 3,2 4,0 4,1 4,2 5,0 5,1 5,2
# 4 -> 3,3 3,4 3,5 4,3 4,4 4,5 5,3 5,4 5,5 
# 5 -> 3,6 5,7 5,8 
 
# 6 -> 6,0 7,0 8,0
# 7
# 8