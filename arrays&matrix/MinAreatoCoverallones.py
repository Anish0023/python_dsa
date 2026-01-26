'''
The goal is to find the smallest rectangle that covers all the 1’s in the grid.

When we think about it, such a rectangle is completely determined by:

The topmost row that contains a 1.
The bottommost row that contains a 1.
The leftmost column that contains a 1.
The rightmost column that contains a 1.
Once we know these boundaries, the rectangle is fixed, and its area is simply:

height × width = (maxRow - minRow + 1) × (maxCol - minCol + 1)
'''

class Solution(object):
    def minimumArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m , n = len(grid), len(grid[0])
        minRow, maxRow = m , -1
        minCol, maxCol = n , -1

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    minRow = min(minRow,i)
                    maxRow = max(maxRow,i)
                    minCol = min(minCol, j)
                    maxCol = max(maxCol, j)
        return (maxRow - minRow + 1) * (maxCol - minCol + 1)
        
if __name__ == "__main__":
    sol = Solution()
    print(sol.minimumArea([[0, 0, 0, 0], [0, 1, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]]))  # Output: 6
    print(sol.minimumArea([[1]]))  # Output: 1
    print(sol.minimumArea([[0]]))  # Output: 0