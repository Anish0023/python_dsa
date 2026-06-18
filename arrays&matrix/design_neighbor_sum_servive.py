'''
You are given a n x n 2D array grid containing distinct elements in the range [0, n2 - 1].

Implement the NeighborSum class:

NeighborSum(int [][]grid) initializes the object.
int adjacentSum(int value) returns the sum of elements which are adjacent neighbors of value, 
that is either to the top, left, right, or bottom of value in grid.
int diagonalSum(int value) returns the sum of elements which are diagonal neighbors of
 value, that is either to the top-left, top-right, bottom-left, or bottom-right of value in grid.

'''
from typing import List
class NeighborSum:

    def __init__(self, grid: List[List[int]]):
        self.grid = grid
        self.rows, self.cols =  len(grid), len(grid[0])
        

    def adjacentSum(self, value: int) -> int:
        row, col = float('inf') , float('inf') 
        directions = [[0,1],[1,0],[-1,0],[0,-1]]
        for i in range(self.rows):
            for j in range(self.cols):
                if self.grid[i][j] == value:
                    row, col = i , j
        sums = 0
        for dr, dc in directions:
            if (row + dr) in range(self.rows) and (col + dc) in range(self.cols):
                sums+=self.grid[row + dr][col + dc]
        return sums

    def diagonalSum(self, value: int) -> int:
        row, col = float('inf') , float('inf') 
        directions = [[-1,1],[1,-1],[-1,-1],[1,1]]
        for i in range(self.rows):
            for j in range(self.cols):
                if self.grid[i][j] == value:
                    row, col = i , j
        sums = 0
        for dr, dc in directions:
            if (row + dr) in range(self.rows) and (col + dc) in range(self.cols):
                sums+=self.grid[row + dr][col + dc]
        return sums

if __name__ == "__main__":
    grid = [[1,2,3],[4,5,6],[7,8,9]]
    obj = NeighborSum(grid)
    print(obj.adjacentSum(4))
    print(obj.diagonalSum(5))