class Solution:
    def smallestNumber(self, n: int) -> int:
        # checking for strictly greater nearest power of two and minus one
        # using OR to increment the number
        while n & (n + 1):
            n |= (n + 1)
        return n
if __name__ == "__main__":
    s = Solution()
    n = 3
    print(f"Smallest number with all set bits greater than or equal to {n} is: {s.smallestNumber(n)}")