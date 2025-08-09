class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        if n == 1:
            return True
        if n%2 != 0:
            return False
        
        return self.isPowerOfTwo(n//2)
    
    def isPowerOfTwoIterative(self, n):
        #using bit manipulation
        '''
        notice that in bits every power of two has only one bit set to 1 so i
        f we subtract 1 from it, all bits to the right of that bit will be set to 1
        and the bit itself will be set to 0. So if we do a bitwise AND operation
        between n and n-1, it will be 0 only if n is a power of two.
        Example: 8 = 1000, 7 = 0111, 1000 & 0111 = 0000
        9 = 1001, 8 = 1000, 1001 & 1000 = 1000 != 0
        16 = 10000, 15 = 01111, 10000 & 01111 = 00000
        18 = 10010, 17 = 10001, 10010 & 10001 = 10000 != 0
        So we can check if n is greater than zero and n & (n-1) == 0
        '''
        return n > 0 and (n & (n-1)) == 0
if __name__ == "__main__":
    sol = Solution()
    print(sol.isPowerOfTwo(16))
    print(sol.isPowerOfTwoIterative(18))