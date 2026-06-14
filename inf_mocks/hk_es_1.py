'''
You’re given an array A of n integers and q queries.
Each query can be one of the following two types:
•
Type 1 Query: (1, l, r) - Replace A[i] with
(i-l+1)*A[l] for each index i, where l <= i <= r.
•
Type 2 Query: (2, l, r) - Calculate the sum of the
elements in A from index l to index r.
Find the sum of answers to all type 2 queries. Since
answer can be large, return it modulo 109+7.
'''
import sys
sys.stdout = open('/Users/aniiiish/Documents/Projects/python_dsa/inf_mocks/output.txt', 'w')
sys.stdin = open('/Users/aniiiish/Documents/Projects/python_dsa/inf_mocks/input.txt','r')

def solve(A , queries):
    sum_ans = 0
    for query in queries:
        check = query[0]
        if check == 1:
            l, r = query[1], query[2]
            for i in range(l, r + 1):
                A[i] = (i - l + 1) * A[l]
        elif check == 2:
            l, r = query[1], query[2]
            for i in range(l, r + 1):
                sum_ans += A[i]
    return sum_ans % (10**9 + 7) 

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        A = []
        for i in range(n):
            A.append(int(input()))
        q = int(input())
        queries = []
        for i in range(q):
            queries.append(list(map(int, input().split())))
        print(solve(A, queries))
        

if __name__ == "__main__":
    main()
    
  