'''
using the concept of three pointers, we can start from the end of both arrays 
and compare the elements, placing the larger one at the end of nums1. 
This way, we can avoid overwriting any elements in nums1 that we haven't compared yet. 
We continue this process until we've gone through all elements in nums2, ensuring 
that nums1 is fully merged and sorted.

'''
from typing import List
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        n1 = m - 1
        n2 = n - 1
        n3 = m + n - 1

        while n2 >= 0:
            if n1 >= 0 and nums1[n1] > nums2[n2]:
                nums1[n3] = nums1[n1]
                n3 -= 1
                n1 -= 1
            else:
                nums1[n3] = nums2[n2]
                n3 -= 1
                n2 -= 1
if __name__=='__main__':
    nums1 = [1,2,3,0,0,0]
    m = 3
    nums2 = [2,5,6]
    n = 3
    sol = Solution()
    sol.merge(nums1,m,nums2,n)
    print(nums1)