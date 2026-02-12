from typing import List
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l , r = 0 , len(nums) - 1
        ans  = float('inf')
        while l <= r:
            m = (l + r)// 2
            # take the minimum from the sorted half i.e either left or right
            if nums[l] <= nums[m]:
                ans = min(ans , nums[l])
                l = m + 1
            else:
                ans = min(ans ,nums[m])
                r = m - 1
        return ans 
if __name__ == '__main__':
    sol = Solution()
    print(sol.findMin([3, 4, 5, 1, 2]))  # Output: 1
    print(sol.findMin([4, 5, 6, 7, 0, 1, 2]))  # Output: 0
    print(sol.findMin([11, 13, 15, 17]))  # Output: 11