'''
here we need to find all the permutations of a given list of numbers
we swap each element with the current index and backtrack to find all permutations'''
from typing import List
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def backtrack(idx):
            if idx == len(nums):
                ans.append(nums[:])
            
            for i in range(idx,len(nums)):
                nums[idx], nums[i] = nums[i] , nums[idx]
                # so when you are retrieving you reach the original state
                #backtrack in order to retain the original array
                backtrack(idx + 1)
                nums[idx], nums[i] = nums[i] , nums[idx]
        backtrack(0)
        return ans
    
if __name__ == "__main__":
    nums = [1,2,3]
    sol = Solution()
    result = sol.permute(nums)
    print("All permutations of", nums, "are:", result)