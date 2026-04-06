from typing import List
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        #--------- BRUTE FORCE -----------------------
        # for i in range(len(nums)):
        #     for j in range(i +1, len(nums)):
        #         if nums[i] == nums[j] and abs(i - j) <= k:
        #             return True
        # return False
        # -------------HASHMAP------------------------
        # visited = {}
        # for i, val in enumerate(nums):
        #     if val in visited and abs(i - visited[val]) <= k:
        #         return True
        #     else:
        #         visited[val] = i
        # return False
        # --------------SLIDING WINDOW--------------------
        window = set()
        for i in range(len(nums)):
            if nums[i] in window:
                return True
            window.add(nums[i])
            if len(window) > k:
                window.remove(nums[i - k])
        return False
if __name__ == '__main__':
    sol = Solution()
    print(sol.containsNearbyDuplicate([1,2,3,1], 3)) # True
    print(sol.containsNearbyDuplicate([1,0,1,1], 1)) # True
    print(sol.containsNearbyDuplicate([1,2,3,1,2,3], 2)) # False