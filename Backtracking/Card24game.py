class Solution(object):
    def judgePoint24(self, cards):
        """
        :type cards: List[int]
        :rtype: bool
        """
        epsilon = 1e-6
        def solve(nums):
            #base case
            if len(nums) == 1:
                return abs(nums[0] - 24) < epsilon
            #picking any two numbers
            for i in range(len(nums)):
                for j in range(len(nums)):
                    if i == j:
                        continue
                    
                    newList = [nums[k] for k in range(len(nums)) if k != i and k != j]
                    a, b = nums[i] , nums[j]
                    #add
                    if solve(newList + [a + b]) : return True
                    #subtract
                    if solve(newList + [a - b]) : return True
                    if solve(newList + [b - a]) : return True
                    #multiply
                    if solve(newList + [a * b]) : return True
                    #divide (a/b and b/a)
                    if b != 0 and solve(newList + [a/b]): return True
                    if a != 0 and solve(newList + [b/a]): return True
            return False
        return solve([float(c) for c in cards])

# Example usage:
if __name__ == "__main__":
    solution = Solution()
    cards = [4, 1, 8, 7]
    print(solution.judgePoint24(cards))  # Output: True
    cards = [1, 2, 1, 2]
    print(solution.judgePoint24(cards))  # Output: False
    '''
    Pick any two numbers from the list,
    apply all four operations (+, -, *, /) on them,
    replace those two numbers with the new result,
    repeat with the new shorter list until only one number remains.
    If that number is 24, return True; otherwise, return False.
    
    '''