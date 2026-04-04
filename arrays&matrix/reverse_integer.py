class Solution:
    def reverse(self, x: int) -> int:
        def helper(x):
            rev = 0
            while x > 0:
                rem = x % 10
                rev =  rev*10 + rem
                x //=10
            return rev
    
        if x > 0:
            ans = helper(x)
            if ans > 2**31 - 1:
                return 0
        else:
            ans = -helper(-x)
            if ans < -2**31:
                return 0
        return ans
if __name__ == '__main__':
    sol = Solution()
    print(sol.reverse(123)) # 321
    print(sol.reverse(-123)) # -321