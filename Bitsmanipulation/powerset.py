#generate all possible subsets of a set using bit manipulation
from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans= []
        subsets_cnt = 1 << n # 2^n subsets
        for num in range(subsets_cnt):
            subsets= []
            for i in range(n):
                # checking if it is a non-zero number then append the subset
                if (num & (1 << i)):
                    subsets.append(nums[i])
            ans.append(subsets)
        return ans 
if __name__ == "__main__":
    nums = [1,2,3]
    print(Solution().subsets(nums))
