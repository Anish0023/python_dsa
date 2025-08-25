class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        n , m = len(matrix), len(matrix[0])
        r , c = 0, 0
        ans = []
        for _ in range(n * m):
            ans.append(matrix[r][c])
            if (r + c) % 2 == 0:
                if c == m - 1:
                    r += 1
                elif r == 0:
                    c += 1
                else:
                    r -= 1
                    c += 1
            else:
                if r == n - 1:
                    c += 1
                elif c == 0:
                    r += 1
                else:
                    c -= 1
                    r += 1
        return ans
if __name__ == "__main__":
    sol = Solution()
    print(sol.findDiagonalOrder([[1,2,3],[4,5,6],[7,8,9]]))  # Output: [1,2,4,7,5,3,6,8,9]
    print(sol.findDiagonalOrder([[1,2],[3,4]]))  # Output: [1,2,3,4]
    print(sol.findDiagonalOrder([[1]]))  # Output: [1]
    print(sol.findDiagonalOrder([[1,2,3,4,5]]))  # Output: [1,2,3,4,5]
    print(sol.findDiagonalOrder([[1],[2],[3],[4],[5]]))  # Output: [1,2,3,4,5]
'''
The trick is here while traversing the matrix into a new one
make sure when we if row + col is even we go up right
else we go down left

'''