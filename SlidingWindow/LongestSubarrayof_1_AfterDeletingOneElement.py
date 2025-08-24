'''Given a binary array nums, you should delete one element from it.
longest subarray of atmost one zero

'''
class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        zero_cnt  = 0
        l = 0
        max_len = 0

        for r in range(len(nums)):
            if nums[r] == 0:
                zero_cnt += 1
            while zero_cnt > 1:
                if nums[l] == 0:
                    zero_cnt -= 1
                l += 1
            max_len = max(max_len, r - l)
        return max_len
if __name__ == "__main__":
    sol = Solution()
    print(sol.longestSubarray([1,1,0,1]))  # Output: 3
    print(sol.longestSubarray([0,1,1,1,0,1,1,0,1]))  # Output: 5
    print(sol.longestSubarray([1,1,1]))  # Output: 2
    print(sol.longestSubarray([1,1,0,0,1,1,1,0,1]))  # Output: 4
    print(sol.longestSubarray([0,0,0]))  # Output: 0