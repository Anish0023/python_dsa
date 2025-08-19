class Solution(object):
    def zeroFilledSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i, ans, n  = 0, 0, len(nums)
        while i < n:
            cnt = 0
            while i < n and nums[i] == 0:
                cnt += 1
                i += 1
                ans += cnt
            i += 1
        return ans

if __name__ == "__main__":
    sol = Solution()
    print(sol.zeroFilledSubarray([1, 3, 0, 0, 2, 0, 0, 4]))  # Output: 6
    print(sol.zeroFilledSubarray([0, 0, 0, 2, 0, 0]))        # Output: 9
    print(sol.zeroFilledSubarray([1, 2, 3]))                 # Output: 0