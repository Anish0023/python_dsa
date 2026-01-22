'''
Docstring for Greedy.sellupto2

Watch Trading for Maximum Profit

You are given N days, numbered from 1 to N.
On the i-th day, the market selling price of a watch is Aᵢ coins.

Initially, you own 0 watches.

Each day consists of the following two events in order:

You receive exactly one watch for free.

You may choose to sell at most two watches that you currently own, each at a price of Aᵢ coins.

You are allowed to keep watches for future days and sell them later if you wish.
'''
# cook your dish here
import heapq
def solve(arr, n):
    max_heap , watches, profit = [] , 0 , 0
    for price in reversed(arr):
        heapq.heappush(max_heap, -price)
        heapq.heappush(max_heap, -price)
        
        watches += 1
        
        if watches > 0 and max_heap:
            best_price = -heapq.heappop(max_heap)
            profit += best_price
            watches -= 1
    return profit
                
    
    
def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int , input().split()))
        ans = solve(arr, n)
        print(ans)

if __name__ == '__main__':
    main()
