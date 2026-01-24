'''
Docstring for binarySearch.FindPeakin2d
A peak element in a 2D grid is an element that is strictly greater than all of its adjacent neighbors to the left, right, top, and bottom.

Given a 0-indexed m x n matrix mat where no two adjacent cells are equal, find any peak element mat[i][j] and return the length 2 array [i,j].

You may assume that the entire matrix is surrounded by an outer perimeter with the value -1 in each cell.

You must write an algorithm that runs in O(m log(n)) or O(n log(m)) time.
'''


from typing import List
class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        n , m = len(mat) , len(mat[0])
        def isPeak(mat , row , col, n , m):
            dr = [[1,0], [-1,0],[0,-1],[0,1]]
            for dx,dy in dr:
                new_r = row + dx
                new_c = col + dy
                if new_r in range(n) and new_c in range(m) and mat[new_r][new_c] > mat[row][col]:
                    return False
            return True
# Needs optimization using binary search
        for r in range(n):
            for c in range(m):
                if isPeak(mat , r , c, n ,m):
                    return [r, c]
        return [-1 ,-1] 
if __name__ == '__main__':
    sol = Solution()
    mat = [[1,4],[3,2]]
    print(sol.findPeakGrid(mat))  # Output: [0, 1]
    
    mat = [[10,20,15],[21,30,14],[7,16,32]]
    print(sol.findPeakGrid(mat))  # Output: [1, 1] or [2, 2]

        