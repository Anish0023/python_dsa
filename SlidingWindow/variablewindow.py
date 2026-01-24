'''
Docstring for SlidingWindow.variablewindow
find the longest subrray with sum at most k
'''

class Solution:
    def variableWindow(self, arr, k):
        n = len(arr)
        l , r = 0 , 0
        sub_sum , max_len = 0 ,  0
        while r < n:
            sub_sum += arr[r]
            while sub_sum > k: # optimize here by replacing while with IF  when length is asked ,in case of subarray we need while
                sub_sum -= arr[l]
                l += 1
            if sub_sum <= k:
                max_len = max(max_len , r - l + 1)
            r += 1
        return max_len

    

if __name__ == "__main__":
    sol = Solution()
    arr = [1,2,3,4,5]
    k = 9
    print(sol.variableWindow(arr, k))  # Output: 3 (subarray [
