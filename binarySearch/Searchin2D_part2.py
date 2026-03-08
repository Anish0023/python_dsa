'''
here start with the top right corner of the matrix.Then reduce search space 
Start at the top-right cell.
If the current value is greater than the target, move left.
If less, move down.
Repeat until found or bounds exceeded.
This avoids binary search and leverages the matrix structure for an efficient solution.
'''

from typing import List
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r = 0
        c = len(matrix[0]) - 1
        while r < len(matrix) and c >= 0:
            if matrix[r][c] == target:
                return True
            elif matrix[r][c] > target:
                c -= 1
            else:
                r += 1
        return False
if __name__ == '__main__':
    sol = Solution()
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    target = 3
    print(sol.searchMatrix(matrix , target))  # Output: True
    
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    target = 13
    print(sol.searchMatrix(matrix , target))  # Output: False