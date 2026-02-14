class Solution:
    def scoreBalance(self, s: str) -> bool:
        '''def score(ch):
            return ord(ch) - ord('a') + 1
        scores = []
        for ch in s:
            score_calculated = score(ch)
            scores.append(score_calculated)
        left_sum , right_sum = 0 , sum(scores)
        for i in range(len(s)):
            score = scores[i]
            left_sum += score
            right_sum -= score
            if left_sum == right_sum:
                return True
        return False'''
        def score(ch):
            return ord(ch) - ord('a') + 1
        total_score = 0
        for ch in s:
            total_score += score(ch)
        if total_score % 2 != 0: return False
        prefix_sum = 0
        for ch in s:
            prefix_sum += score(ch)
            if prefix_sum == (total_score//2):
                return True
        return False
if __name__ == '__main__':
    sol = Solution()
    print(sol.scoreBalance("abcde"))  # Output: False
    print(sol.scoreBalance("abcdeedcba"))  # Output: True
    print(sol.scoreBalance("aabbcc"))  # Output: True