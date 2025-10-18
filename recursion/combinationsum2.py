'''
here we can pick each element only once, and the order of elements does not matter
to avoid duplicates we sort the array and skip the  same elements
'''
from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res, ds = [], []
        candidates.sort()

        def findComb2(idx, target):
            if target == 0:
                res.append(ds[:])
                return
            for i in range(idx, len(candidates)):
                if i > idx and candidates[i] == candidates[i - 1]:
                    continue
                if candidates[i] > target:
                    break
                ds.append(candidates[i])
                findComb2(i + 1, target - candidates[i])
                ds.pop()


        findComb2(0, target)
        return res
if __name__ == "__main__":
    candidates = [10,1,2,7,6,1,5]
    target = 8
    sol = Solution()
    result = sol.combinationSum2(candidates, target)
    print("Unique combinations that sum to", target, "are:", result)