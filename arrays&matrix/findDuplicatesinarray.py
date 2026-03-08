'''
the brute force approach would be to use a hash map to count 
the occurrences of each number in the array.

The optimal wihout using extra space is to iterate through the array 
and for each number mark the index corresponding to that number as negative.
then if we encounter a number whose corresponding index is already negative,
store that number in the result list as it is a duplicate.
'''
from typing import List
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []
        for num in nums:
            idx = abs(num) - 1
            if nums[idx] < 0:
                ans.append(abs(num))
            else:
                nums[idx] = -nums[idx]
        return ans
if __name__ == '__main__':
    sol = Solution()
    print(sol.findDuplicates([4,3,2,7,8,2,3,1]))  # Output: [2,3]
    print(sol.findDuplicates([1,1,2]))  # Output: [1]