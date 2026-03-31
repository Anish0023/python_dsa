'''
The dutch national flag problem is a classic algorithmic problem 
that involves sorting an array of three distinct values 
(often represented as 0s, 1s, and 2s) in linear time and constant space. 
The goal is to rearrange the elements in such a way that all 0s come first, 
followed by all 1s, and then all 2s.
we use the binary search approach to solve this problem. We maintain three pointers:
when mid is 0, we swap it with low and move both pointers forward.
when mid is 1, we just move the mid pointer forward.
when mid is 2, we swap it with high and move the high pointer backward.
'''
from typing import List
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ### dutch national flag algorithm
        low = 0
        mid = 0
        high = len(nums) - 1
        while mid <= high:
            if nums[mid] == 0:
                (nums[low],nums[mid]) = (nums[mid],nums[low])
                low+=1
                mid+=1

            elif nums[mid] == 1:
                mid+=1

            else:
                (nums[mid],nums[high]) = (nums[high],nums[mid])
                high-=1
        return nums
if __name__ == '__main__':
    sol = Solution()
    print(sol.sortColors([2,0,2,1,1,0]))
    print(sol.sortColors([2,0,1]))
    
