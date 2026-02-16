from typing import List
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(u):
            for v in range(n):
                if isConnected[u][v] and  visited[v] == 0:
                    visited[v] = 1
                    dfs(v)
        n = len(isConnected)
        visited = [0]*n
        cnt = 0
        for u in range(n):
            if visited[u] != 1:
                dfs(u)
                cnt  += 1
        return cnt
if __name__ == '__main__':
    isConnected = [[1,1,0],[1,1,0],[0,0,1]]
    print(Solution().findCircleNum(isConnected))  # Output: 2
    isConnected = [[1,0,0],[0,1,0],[0,0,1]]
    print(Solution().findCircleNum(isConnected))  # Output: 3