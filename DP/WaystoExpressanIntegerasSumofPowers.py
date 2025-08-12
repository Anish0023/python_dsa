class Solution(object):
    def numberOfWays(self, n, x):
        """
        :type n: int
        :type x: int
        :rtype: int
        """
        '''
        Think of it as knapsack problem where you can take or skip each number raised to the power x.
        We use recursion with memoization to count the number of ways to express n as a sum of powers.
        - If remaining is 0, we found a valid way.
        - If remaining is negative, it's not valid.
        - For each number starting from 1, we can either take it raised to x or skip it.
        - We use a dictionary to memoize results for (remaining, num) pairs to avoid recomputation.
        '''
        M = 10**9 + 7
        memo = {}  # dictionary for memoization

        def solve(remaining, num):
            if remaining == 0:
                return 1
            if remaining < 0:
                return 0
            if (remaining, num) in memo:
                return memo[(remaining, num)]

            currPower = pow(num, x)
            if currPower > remaining:
                return 0

            # take num^x
            take = solve(remaining - currPower, num + 1)

            # skip num^x
            skip = solve(remaining, num + 1)

            memo[(remaining, num)] = (take + skip) % M
            return memo[(remaining, num)]
        return solve(n, 1)
if __name__ == "__main__":
    sol = Solution()
    n = 10
    x = 2
    print(sol.numberOfWays(n, x))  # Output: 1 (10 = 3^2 + 1^2)
    n = 100
    x = 3
    print(sol.numberOfWays(n, x))