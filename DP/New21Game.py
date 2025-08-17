class Solution(object):
    def new21Game(self, n, k, maxPts):
        """
        :type n: int
        :type k: int
        :type maxPts: int
        :rtype: float
        """
    
        if k == 0 or n >= k - 1 + maxPts:
            return 1.0

        dp = [0.0] * maxPts
        dp[0] = 1.0

        window_sum = 1.0
        result = 0.0

        for i in range(1, n + 1):
            prob = window_sum / maxPts

            if i < k:
                window_sum += prob
            else:
                result += prob

            if i >= maxPts:
                window_sum -= dp[i % maxPts]

            dp[i % maxPts] = prob

        return result
if __name__ == "__main__":
    sol = Solution()
    n = 10
    k = 1
    maxPts = 10
    print(sol.new21Game(n, k, maxPts))  # Output: 1.0 (always win)
    n = 6
    k = 3
    maxPts = 5
    print(sol.new21Game(n, k, maxPts))
'''
Intuition
The problem is about calculating the probability that Alice ends up with a score of at most N when she keeps drawing numbers between 1 and maxPts until her score reaches at least K. At first glance, this looks similar to dynamic programming on probabilities because the outcome of each draw depends on the results of previous draws. The key idea is that the probability of reaching a score i can be derived from the probabilities of reaching earlier scores within a sliding window of size maxPts.
Instead of recalculating probabilities for each range repeatedly, we maintain a running sum of the last maxPts probabilities, which allows us to update efficiently. This way, we can build probabilities step by step and finally add up the ones that represent valid outcomes (scores between K and N).
Approach
We use dynamic programming with a sliding window to efficiently calculate probabilities. Let dp[i] represent the probability of reaching exactly i points. Initially, dp[0] = 1 since Alice always starts with 0 points. For every next score i, its probability comes from all possible scores that could have led to it in one draw, i.e., dp[i] = (dp[i-1] + dp[i-2] + ... + dp[i-maxPts]) / maxPts. Directly computing this sum would be too slow, so we maintain a running total called windowSum, which keeps track of the last maxPts probabilities.
At each step:

We compute prob = windowSum / maxPts as the probability for i.

If i < K, Alice can still draw more, so we add this probability into windowSum.

If i >= K, Alice stops drawing, so we add this probability to the final result.

To maintain the window size, if i >= maxPts, we remove the oldest probability from windowSum.

By repeating this process up to N, we efficiently compute the result without recalculating large sums repeatedly.

Complexity
Time complexity: O(N)
Space complexity: O(maxPts)
'''