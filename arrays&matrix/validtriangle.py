from typing import List
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        ans = 0
        for i in range(2, len(nums)):
            left , right = 0, i - 1
            while left < right:
                if nums[left] + nums[right] > nums[i]:
                    ans += right - left
                    right -= 1
                else:
                    left += 1
        return ans
if __name__ == '__main__':
    sol = Solution()
    print(sol.triangleNumber([2, 2, 3, 4]))  # Output: 3
    print(sol.triangleNumber([4, 2, 3, 4]))  # Output: 4
    print(sol.triangleNumber([1, 1, 3, 4]))  # Output: 0

