'''
here we can pick the element multiple times, and the order of elements does not matter
if we are not able to pick the element we move to next index
'''
from typing import List
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res, ds = [], []
        def findComb(idx,target):
            if idx  == len(candidates):
                if target == 0:
                    res.append(ds[:])
                return
            if candidates[idx] <= target:
                ds.append(candidates[idx])
                #pick
                findComb(idx,target - candidates[idx])
                ds.pop()
            # not pick
            findComb(idx + 1, target)
        findComb(0,target)
        return res
if __name__ == "__main__":
    candidates = [2,3,6,7]
    target = 7
    sol = Solution()
    result = sol.combinationSum(candidates, target)
    print("Combinations that sum to", target, "are:", result)