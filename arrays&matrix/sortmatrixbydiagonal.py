'''
notice how we are traversing the diagonals in order to sort the lower 
half in descending order and upper half in ascending order.
'''
class Solution(object):
    def sortMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[List[int]]
        """
        n = len(grid)
        #lower half including diagonal
        for i in range(n):
            tmp = [grid[i + j][j] for j in range(n -  i)]
            print(tmp)
            tmp.sort(reverse = True)
            for j in range(n-i):
                grid[i + j][j] = tmp[j]
            
        #upper half 
        for i in range(1,n):
            tmp = [ grid[j][i + j] for j in range(n-i)]
            print(tmp)
            tmp.sort()
            for j in range(n - i):
                grid[j][i + j] = tmp[j]
        return grid
if __name__ == "__main__":
    grid = [[3, 3, 1, 1], [2, 2, 1, 2], [1, 1, 1, 2], [1, 1, 1, 2]]
    print(Solution().sortMatrix(grid))  
