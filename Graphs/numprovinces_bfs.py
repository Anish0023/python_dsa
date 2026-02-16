from typing import List
from collections import deque
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def bfs(u):
            q = deque()
            q.append(u)
            visited[u] = 1
            while q:
                node = q.popleft()
                for child in range(n):
                    if isConnected[node][child] and visited[child] != 1:
                        visited[child] = 1
                        q.append(child)


            
        n = len(isConnected)
        visited = [0]*n
        cnt = 0
        for u in range(n):
            if visited[u] != 1:
                bfs(u)
                cnt  += 1
        return cnt
if __name__ == '__main__':
    isConnected = [[1,1,0],[1,1,0],[0,0,1]]
    print(Solution().findCircleNum(isConnected))  # Output: 2
    isConnected = [[1,0,0],[0,1,0],[0,0,1]]
    print(Solution().findCircleNum(isConnected))  # Output: 3