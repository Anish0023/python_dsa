'''
Hypothetically, flatten the array and try to implement binary search on it.
The index of the middle element can be calculated as mid = (l + h) // 2.
To get the row and column of the middle element,
we can use row = mid // m and col = mid % m, 
where m is the number of columns in the matrix. 
This way, we can compare the middle element with the target and 
adjust our search range accordingly until we find the target or exhaust the search space.
'''
from typing import List
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n , m = len(matrix) , len(matrix[0])
        l , h = 0 , (n * m) - 1
        while l <= h:
            mid = (l + h)// 2
            row , col = mid//m , mid%m
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                l = mid + 1
            else:
                h = mid - 1
        return False
if __name__ == '__main__':
    sol = Solution()
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    target = 3
    print(sol.searchMatrix(matrix , target))  # Output: True
    
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    target = 13
    print(sol.searchMatrix(matrix , target))  # Output: False