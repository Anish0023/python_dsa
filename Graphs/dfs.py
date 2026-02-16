
def dfs_graph(V,adj):
    visited = [False] * V
    result = []
    
    def dfs(node):
        visited[node] = True
        result.append(node)
        
        for neighbor in adj[node]:
            if not visited[neighbor]:
                dfs(neighbor)
    
    for i in range(V):
        if not visited[i]:
            dfs(i)
    
    return result
if __name__ == '__main__':
    V = 5
    adj = [[1, 2], [0, 3], [0, 4], [1], [2]]
    print(dfs_graph(V, adj))  # Output: [0, 1, 3, 2, 4]