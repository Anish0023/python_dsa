'''
Docstring for binarySearch.FindPeak
A peak element is an element that is strictly greater than its neighbors.

Given a 0-indexed integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.

You may imagine that nums[-1] = nums[n] = -∞. In other words, an element is always considered to be strictly greater than a neighbor that is outside the array.

You must write an algorithm that runs in O(log n) time.

'''

from typing import List
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l , r = 0 , len(nums) - 1
        while l < r:
            m = (l + r) >> 1
            if nums[m - 1] <= nums[m] >= nums[m+1]:
                return m
            elif nums[m] < nums[m + 1]:
                l = m + 1
            else:
                r = m 
        return l
if __name__ == '__main__':
    sol = Solution()
    arr1 = [1,2,3,1]
    arr2 =  [1,2,1,3,5,6,4]
    print(sol.findPeakElement(arr1))
    print(sol.findPeakElement(arr2))
        