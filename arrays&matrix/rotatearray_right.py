from typing import List
'''
BRUTE FORCE
Time complexity: O(n*k) 
def rotate(self,nums,k):
    n = len(nums)
    k%=n
    for _ in range(k):
        last = nums.pop()
        nums.insert(0,last)

'''
class Solution:
    def reverse(self,nums,l ,r):
        while l < r:
            nums[l] ,nums[r] = nums[r] , nums[l]
            l += 1
            r -= 1
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k%=n
        self.reverse(nums,0 ,n - 1)
        self.reverse(nums,0, k - 1)
        self.reverse(nums,k, n - 1)
        print(nums)
if __name__ == '__main__':
    sol = Solution()
    print(sol.rotate([1,2,3,4,5,6,7], 3))
    print(sol.rotate([-1,-100,3,99], 2))

'''
class Solution:
    def rotate(self, nums, k):
        k = k % len(nums)          # Normalize k
        nums[:] = nums[-k:] + nums[:-k]   # Slice & combine

'''