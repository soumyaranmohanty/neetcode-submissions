class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_hm ={}
        sub_mat=3
        #row_set = set()
        board_row = len(board)
        board_col = len(board[0])
        #print(board_row, board_col)
        for row in range(board_row):
            #print(row,  " : ", )
            row_set = set()
            for col in range(board_col):
                #print(board[row][col])
                if board[row][col] in row_set:
                    return False
                if board[row][col]==".":
                    continue
                row_set.add(board[row][col])

        for col in range(board_col):
            #print(col,  " : ")
            col_set = set()
            for row in range(board_row):
                #print(board[row][col])
                if board[row][col] in col_set:
                    return False
                if board[row][col]==".":
                    continue
                col_set.add(board[row][col])

        for i in range(0,3):
            for j in range(0,3):
                row_start=i*3
                row_end=i*3+2

                col_start=j*3
                col_end=j*3+2
                sub_row_set = set()
                for row in range(row_start, row_end+1):
                    
                    for col in range(col_start, col_end+1):
                        if board[row][col] in sub_row_set:
                            return False
                        if board[row][col]==".":
                            continue
                        sub_row_set.add(board[row][col])




        return True
        
        