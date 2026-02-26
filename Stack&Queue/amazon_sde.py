from collections import deque
import math

from collections import deque

def max_items(m, costs):
    q = deque()
    
    # store (current_cost, base_cost)
    for c in costs:
        q.append([c, c])
    
    count = 0
    
    while q:
        curr, base = q.popleft()
        
        # early stop condition
        if m < curr:
            break
        
        # buy
        m -= curr
        count += 1
        
        # update cost (linear growth)
        new_cost = curr + base
        
        # push back for next pass
        q.append([new_cost, base])
        print(q)
    return count

if __name__=='__main__':
    m = 18
    costs = [2,5,1,1]
    print(max_items(m, costs))  # Output: 4

    m = 25
    costs = [1]
    print(max_items(m, costs))  # Output: 5