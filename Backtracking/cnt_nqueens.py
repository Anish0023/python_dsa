from typing import List
class Solution:
    def countSolutions(self, n: int) -> int:
        def count(col, left_row, upper_diagonal, lower_diagonal):
            if col == n:
                return 1
            total = 0
            for row in range(n):
                if left_row[row] == 0 and lower_diagonal[row + col] == 0 and upper_diagonal[(n - 1) + (col - row)] == 0:
                    left_row[row] = 1
                    lower_diagonal[row + col] = 1
                    upper_diagonal[(n - 1) + (col - row)] = 1
                    total += count(col + 1, left_row, upper_diagonal, lower_diagonal)
                    left_row[row] = 0
                    lower_diagonal[row + col] = 0
                    upper_diagonal[(n - 1) + (col - row)] = 0
            return total

        left_row = [0] * n
        lower_diagonal = [0] * (2 * n - 1)
        upper_diagonal = [0] * (2 * n - 1)
        return count(0, left_row, upper_diagonal, lower_diagonal)
if __name__ == "__main__":
    obj = Solution()
    n = 8
    print("Distinct solutions count:", obj.countSolutions(n))
    