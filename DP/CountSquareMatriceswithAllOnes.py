'''
The biggest square at each cell is limited by the smallest square from the neighbors below,
 to the right, and diagonal right-below. 
 We recursively or iteratively use this relation to count squares efficiently.
 base case is when we reach the edge of the matrix or find a zero.
 if matrix[r][c] is 1 :
    1 + min(dfs(r + 1, c), dfs(r, c + 1), dfs(r + 1, c + 1))
else:
    return 0

'''

class Solution(object):
    def countSquares(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        cache = {}
        rows, cols = len(matrix), len(matrix[0])
        def dfs(r,c):
            if r == rows or c == cols or not matrix[r][c]:
                return 0
            if (r,c) in cache:
                return cache[(r,c)]
            cache[(r,c)] = 1 + min(
                dfs(r + 1, c),
                dfs(r, c + 1),
                dfs(r + 1, c + 1)
            )
            return cache[(r,c)]

        ans = 0
        for r in range(rows):
            for c in range(cols):
                ans += dfs(r,c)
        return ans
if __name__ == "__main__":
    sol = Solution()
    print(sol.countSquares([[0,1,1,1],[1,1,1,1],[0,1,1,1]]))  # Output: 15
    print(sol.countSquares([[1,0,1],[1,1,0],[1,1,0]]))        # Output: 7
    print(sol.countSquares([[0]]))                            # Output: 0