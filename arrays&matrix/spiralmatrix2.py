from typing import List
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        ans = [[0] * n for _ in range(n)]
        cnt = 1
        
        top, bottom = 0, n - 1
        left, right = 0, n - 1
        
        while top <= bottom and left <= right:
            # top row - left to right
            for i in range(left, right + 1):
                ans[top][i] = cnt
                cnt += 1
            top += 1
            
            # right column - top to bottom
            for i in range(top, bottom + 1):
                ans[i][right] = cnt
                cnt += 1
            right -= 1
            
            # bottom row - right to left
            if top <= bottom:
                for i in range(right, left - 1, -1):
                    ans[bottom][i] = cnt
                    cnt += 1
                bottom -= 1
            
            # left column - bottom to top
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    ans[i][left] = cnt
                    cnt += 1
                left += 1
        
        return ans
if __name__ == '__main__':
    sol = Solution()
    print(sol.generateMatrix(3))  # Example usage
 
    

