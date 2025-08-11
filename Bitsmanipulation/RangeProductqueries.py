class Solution(object):
    def productQueries(self, n, queries):
        """
        :type n: int
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        MOD = 10**9 + 7
        powers = []
        res= []
        power = 1
        '''
        n & 1 checks if the least significant bit is 1.
        power starts at 1 (2^0) and doubles each loop.
        If bit is 1, add that power to powers.
        Then shift n right to process the next bit.
        Result: powers contains exactly the powers of 2 that sum to n, in ascending order.
        '''
        while n > 0:
            if n & 1:
                powers.append(power)
            power <<= 1
            n >>= 1
        for l,r in queries:
            if l < 0 or r >= len(powers):
                res.append(-1)
                continue
            p = 1
            for j in range(l,r+1):
                p = (p * powers[j])%MOD
            res.append(p)

        return  res
if __name__ == "__main__":
    sol = Solution()
    n = 5
    m =  15
    queries2 = [[0,1],[2,2],[0,3]]
    queries = [[0, 1], [2, 2]]
    print(sol.productQueries(n, queries))
    print(sol.productQueries(m, queries2))

