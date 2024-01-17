class Solution:
    def rowCreator(self, board, xCord, yCord):
        newRow = []
        for k in range(0,3):
            newRow.append(board[xCord][yCord+k])
            newRow.append(board[xCord+1][yCord+k])
            newRow.append(board[xCord+2][yCord+k])
        return newRow
    def isRowValid(self,row):
        for num in row:
            if num.isdigit():
                if row.count(num) > 1:
                    return False
        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rotatedBoard = list(zip(*board))[::1]
        for row in board:
            if self.isRowValid(row) == False:
                return False
        for row in rotatedBoard:
            if self.isRowValid(row) == False:
                return False
        for x in range(0,7,3):
            for y in range(0,7,3):
                row = self.rowCreator(board,x,y)
                if self.isRowValid(row) == False:
                    return False
        return True


        
        

            
            
        
