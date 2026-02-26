from typing import List
class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        def gcd(a,b):
            while b != 0:
                temp = b
                b = a%b
                a = temp
            return a
        cnt = 0
        for i in range(len(nums)):
            curr_gcd = 0
            for j in range(i , len(nums)):
                curr_gcd = gcd(curr_gcd, nums[j])
                if curr_gcd == k:
                    cnt += 1
        return cnt
if __name__ == '__main__':
    sol = Solution()
    print(sol.subarrayGCD([9,3,1,2,6,3], 3))
    print(sol.subarrayGCD([4], 7))