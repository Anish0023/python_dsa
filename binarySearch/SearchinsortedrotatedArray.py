'''
Docstring for binarySearch.SearchinsortedrotatedArray

Search in Rotated Sorted Array II where the nums dont include duplicates and the array is sorted 
and rotated at some pivot unknown to you beforehand.
'''
from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l , r  =  0 , len(nums) - 1
        while l <= r:
            m = (l + r )// 2
            if nums[m] == target:
                return m
            # if left half is sorted
            if nums[m] >= nums[l]:
                if target >= nums[l] and target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            #if right half is sorted
            else:
                if target > nums[m] and target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
        return -1
if __name__ == "__main__":
    sol = Solution()
    nums = [4,5,6,7,0,1,2]
    target = 0
    result = sol.search(nums, target)
    print(f"Index of target {target} in rotated sorted array is: {result}")

