'''
Docstring for binarySearch.SearchinsortedArray2
Search in Rotated Sorted Array II where the nums include duplicates and the array is sorted 
and rotated at some pivot unknown to you beforehand.
'''
from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l , r  =  0 , len(nums) - 1
        while l <= r:
            m = (l + r )// 2
            if nums[m] == target:
                return True
            #if cant find the sorted half
            if nums[l] == nums[m] == nums[r]:
                r -= 1
                l += 1
                continue
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
        return False
if __name__ == "__main__":
    sol = Solution()
    nums = [2,5,6,0,0,1,2]
    target = 0
    result = sol.search(nums, target)
    print(f"Target {target} found in rotated sorted array: {result}")
