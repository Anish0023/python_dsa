class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:
        score = 0
        for num in nums:
            num.sort()
            num.sort()
        
        for i in range(len(nums[0])):
            maxi = nums[0][i]
            for j in range(len(nums)):
                maxi =  max(maxi,nums[j][i])
            
            score += maxi
        return score