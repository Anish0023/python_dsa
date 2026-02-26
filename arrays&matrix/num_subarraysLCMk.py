from typing import List
class Solution:
    def subarrayLCM(self, nums: List[int], k: int) -> int:
        def gcd(a,b):
            while b != 0:
                temp = b
                b = a%b
                a = temp
            return a
        def lcm(a,b):
            return (a * b)/gcd(a,b)
        cnt = 0
        for i in range(len(nums)):
            curr_lcm = 1
            for j in range(i , len(nums)):
                curr_lcm = lcm(curr_lcm, nums[j])
                if curr_lcm == k:
                    cnt += 1
                # we dont have to calculate as it becomes greater than k , lcm increases not needed
                elif curr_lcm > k:
                    break
        return cnt
if __name__ == '__main__':
    sol = Solution()
    print(sol.subarrayLCM([3,6,2,7,1], 6))
    print(sol.subarrayLCM([3], 2))