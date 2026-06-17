'''
You are given an array A of length N and an
integer k.
It is given that a subarray from l to r is considered
good, if the number of distinct elements in that
subarray doesn’t exceed k. Additionally, an empty
subarray is also a good subarray and its sum is
considered to be zero.
Find the maximum sum of a good subarray.


'''

import sys
sys.stdout = open('/Users/aniiiish/Documents/Projects/python_dsa/inf_mocks/output.txt', 'w')
sys.stdin = open('/Users/aniiiish/Documents/Projects/python_dsa/inf_mocks/input.txt','r')


from collections import defaultdict
import heapq

def maxGoodSubarraySum(A, k):
    n = len(A)

    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i + 1] = prefix[i] + A[i]

    freq = defaultdict(int)
    left = 0
    ans = 0

    # (prefix_sum, index)
    heap = [(0, 0)]

    for right in range(n):
        freq[A[right]] += 1

        while len(freq) > k:
            freq[A[left]] -= 1
            if freq[A[left]] == 0:
                del freq[A[left]]
            left += 1

        # Remove prefixes that are no longer valid
        while heap and heap[0][1] < left:
            heapq.heappop(heap)

        ans = max(ans, prefix[right + 1] - heap[0][0])

        heapq.heappush(heap, (prefix[right + 1], right + 1))

    return ans
def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        k = int(input())
        A = []
        for i in range(n):
            A.append(int(input()))
        print(maxGoodSubarraySum(A,k))
if __name__ == '__main__':
    main()