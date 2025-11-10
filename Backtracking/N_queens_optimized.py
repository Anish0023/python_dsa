from typing import List
class Solution:
    def solve(self, col , board , n , left_row ,upper_diagonal ,lower_diagonal,res):
        if col == n:
            res.append(["".join(row) for row in board])
            return
        #iterating through rows
        for row in range(n):
            # checking safety
            if left_row[row] == 0 and lower_diagonal[row+col] == 0 and upper_diagonal[(n - 1)+(col-row)] == 0:
                #place the queen
                board[row][col] = 'Q'
                left_row[row] = 1
                lower_diagonal[row+col] = 1
                upper_diagonal[(n - 1)+(col-row)] = 1
                #recursion
                self.solve(col + 1 , board , n , left_row ,upper_diagonal ,lower_diagonal,res)
                # backtrack 
                board[row][col] = '.'
                left_row[row] = 0
                lower_diagonal[row+col] = 0
                upper_diagonal[(n - 1)+(col-row)] = 0



    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        #creating the N x N board
        board = [['.' for _ in range(n)] for _ in range(n)]
        #hashing to keep track of the placed queens
        left_row = [0]*n
        lower_diagonal = [0] * (2*n-1)
        upper_diagonal = [0] * (2*n-1)
        self.solve(0,board , n , left_row ,upper_diagonal ,lower_diagonal,res)
        return res
if __name__ == "__main__":
    obj = Solution()
    n = 4
    result = obj.solveNQueens(n)
    for solution in result:
        for row in solution:
            print(row)
        print()
        