'''
You are given an integer array nums. In one move, you can pick an index i where 0 <= i < nums.length and increment nums[i] by 1.

Return the minimum number of moves to make every value in nums unique.

The test cases are generated so that the answer fits in a 32-bit integer.

Example 1:

Input: nums = [1,2,2]
Output: 1
Explanation: After 1 move, the array could be [1, 2, 3].
Example 2:

Input: nums = [3,2,1,2,1,7]
Output: 6
Explanation: After 6 moves, the array could be [3, 4, 1, 2, 5, 7].
It can be shown that it is impossible for the array to have all unique values with 5 or less moves.

TRY to sort the array , and then make the minimum operations required to make the array increasing
in order to make in unique
'''
from typing import List
class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        cnt = 0
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i] >= nums[i + 1]:
                cnt += nums[i] - nums[i + 1] + 1
                nums[i + 1]= nums[i]+1
            else:
                cnt += 0
        return cnt
if __name__=='__main__':
    nums = [3,2,1,2,1,7]
    sol = Solution()
    print(sol.minIncrementForUnique(nums))
    nums2 = [1,2,2]
    print(sol.minIncrementForUnique(nums2))