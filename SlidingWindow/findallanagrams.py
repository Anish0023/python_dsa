from collections import defaultdict
from typing import List

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # Handle the edge case where the pattern is longer than the string
        if len(p) > len(s):
            return []

        # --- Step 1: Create the target fingerprint for 'p' ---
        p_fingerprint = defaultdict(int)
        for char in p:
            p_fingerprint[char] += 1

        result = []
        missing = len(p)   # number of characters still needed
        left = 0

        # --- Step 2 & 3: Build window + slide it ---
        for right in range(len(s)):
            # Character enters the window
            if p_fingerprint[s[right]] > 0:
                missing -= 1
            p_fingerprint[s[right]] -= 1

            # --- Maintain window size equal to len(p) ---
            if right - left + 1 > len(p):
                # Character leaves the window
                if p_fingerprint[s[left]] >= 0:
                    missing += 1
                p_fingerprint[s[left]] += 1
                left += 1

            # --- Step 4: Check for valid anagram ---
            if missing == 0:
                result.append(left)

        return result
if __name__ == '__main__':
    sol = Solution()
    print(sol.findAnagrams('cbaebabacd', 'abc'))  # Example usage
'''
another way to test the function

    def findAnagrams(self, s: str, p: str) -> List[int]:
        # Handle the edge case where the pattern is longer than the string
        if len(p) > len(s):
            return []
        
        # --- Step 1: Create the target fingerprint for 'p' ---
        # We use an array of 26 zeros, one for each letter 'a' through 'z'
        p_fingerprint = [0] * 26
        for char in p:
            p_fingerprint[ord(char) - ord('a')] += 1
            
        result = []
        window_fingerprint = [0] * 26
        
        # --- Step 2: Build the fingerprint for the initial window ---
        for i in range(len(p)):
            window_fingerprint[ord(s[i]) - ord('a')] += 1
            
        # --- Step 3: Compare the first window's fingerprint ---
        if p_fingerprint == window_fingerprint:
            result.append(0)
            
        # --- Step 4: Slide the window across the rest of the string ---
        # We start the loop from where the first window ended
        for i in range(len(p), len(s)):
            # Update the fingerprint:
            # - Increment the count for the new character entering the window
            window_fingerprint[ord(s[i]) - ord('a')] += 1
            # - Decrement the count for the old character leaving the window
            window_fingerprint[ord(s[i - len(p)]) - ord('a')] -= 1
            
            # --- Compare the updated window's fingerprint ---
            if p_fingerprint == window_fingerprint:
                # The start of a valid window is at 'i - len(p) + 1'
                start_index = i - len(p) + 1
                result.append(start_index)
                
        return result

'''