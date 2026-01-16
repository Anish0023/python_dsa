'''
APPROACH
If there are 3 consecutive empty cells i−1
, i
, i+1
, we can place water in cells i−1
 and i+1
 and then move water from cell i
 to all other cells. If there are no such cells, we have to place water on every empty cell.

So if we find substring ''...'' in the array, the answer is 2
, otherwise the answer is the number of empty cells.

Time and memory complexities are O(N)
.
'''

t = int(input())
for _ in range(t):
    n = int(input())
    s = str(input())[:n]
    sub = '...'
    cnt = 0
    if sub in s:
        print(2)
    else:
        for ch in s:
            if ch == '.':
                cnt += 1
        print(cnt)
