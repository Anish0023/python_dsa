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