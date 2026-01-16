'''
Docstring for Backtracking.pathfinding
Path finding problem: Given an × matrix of blocks with a source upper left block, we want to find a path from the
source to the destination(the lower right block). We can only move downwards and to the left. Also, a path is given by 1 and a wall is given
by 0. 
[[1,1,0,0],
 [0,1,1,0],
 [0,0,1,0],
 [0,0,1,1]]
'''
def pathFinder(position, matrix, N):
    if position == (N-1, N-1):
        return [(N-1, N-1)]
    r, c = position
    if r + 1 in range(N) and matrix[r + 1][c] == 1:
        row_path = pathFinder((r + 1,c), matrix, N)
        if row_path:
            return [(r, c)] + row_path
    if c + 1 in range(N) and matrix[r][c + 1] == 1:
        col_path = pathFinder((r, c+1), matrix, N)
        if col_path:
            return [(r, c)] + col_path
if __name__ == '__main__':
    solution = pathFinder((0,0), [[1,1,0,0],
                                 [0,1,1,0],
                                 [0,0,1,0],
                                 [0,0,1,1]], 4)
    print(solution)  # [(0, 0), (0, 1), (1, 1), (1, 2), (2, 2), (3, 2), (3, 3)]
    