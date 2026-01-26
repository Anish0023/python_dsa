import heapq
ans = [3,4,5,2]
sorted_ans = sorted(ans)
n  =  len(sorted_ans)
sorted_ans = sorted_ans[::-1]
print((sorted_ans[0]-1)*(sorted_ans[1]-1))