class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        # using xor to get the bits that need to be flipped
        res = start ^ goal
        #calculate the set bits count 
        cnt = 0
        while res:
            res &= (res - 1)
            cnt += 1
        return cnt
if __name__ == "__main__":
    s = Solution()
    start = 10
    goal = 7
    print(f"Minimum bit flips to convert {start} to {goal}: {s.minBitFlips(start, goal)}")