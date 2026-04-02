'''
assume the input array is sorted, we can use two pointers 
to find the target sum. We can start with one pointer at the 
beginning of the array and another pointer at the end of 
the array. We can calculate the sum of the two numbers at these 
pointers and compare it with the target. If the sum is equal to 
the target, we have found our answer. If the sum is less than 
the target, we need to move the left pointer to the right to 
increase the sum. If the sum is greater than the target, 
we need to move the right pointer to the left to decrease the 
sum. We can continue this process until we find the target or 
until the pointers cross each other. (Assume 1-based index)

'''
from typing import List
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1
        while l  < r:
            sums = numbers[l] + numbers[r]
            if sums == target:
                return [l + 1, r + 1]
            elif sums < target :
                l += 1
            else:
                r -= 1
        return [-1, -1]
if __name__=='__main__':
    sol = Solution()
    print(sol.twoSum([2,7,11,15], 9))
    print(sol.twoSum([2,3,4], 6))
    print(sol.twoSum([-1,0], -1))