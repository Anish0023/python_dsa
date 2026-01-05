from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        def backtrack(idx):
            if idx >= len(nums):
                res.append(subset[:])
                return
            subset.append(nums[idx])
            backtrack(idx+1)
            subset.pop()
            backtrack(idx+1)
        backtrack(0)
        return res


if __name__ == "__main__":
    s = Solution()
    nums = [1, 2, 3]
    print(f"All subsets of {nums} are: {s.subsets(nums)}")