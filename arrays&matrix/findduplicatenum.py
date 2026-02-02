from typing import List
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # phase 1 : detecting the cycle - treating the array as LL
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        # finding cycle entrance (duplicate num)
        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow

if __name__ == '__main__':
    print(Solution().findDuplicate([1,3,4,2,2]))
    print(Solution().findDuplicate([3,1,3,4,2]))