from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        '''
        Try all pairs (i, j). BRUTE FORCE
        Compute area = min(height[i], height[j]) * (j - i).
        Track the maximum.
        Time: O(n²)
        Space: O(1)
        '''
        #optimised
        max_area , l , r = 0 , 0 , len(height) - 1
        while l < r:
            width = r - l
            max_area = max(max_area, width * min(height[l],height[r]))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return max_area
if __name__ == '__main__':
    sol = Solution()
    print(sol.maxArea([1,8,6,2,5,4,8,3,7])) # 49
    print(sol.maxArea([1,1])) # 1
    print(sol.maxArea([4,3,2,1,4])) # 16