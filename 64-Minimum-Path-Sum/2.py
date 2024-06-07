def minPathSum():
    grid = [[1,3,1],
            [1,5,1],
            [4,2,1]]
    
    m, n = len(grid), len(grid[0])

    def traverse(i, j):
        if i == m - 1 and j == n - 1:
            return grid[-1][-1]

        if i < m-1:
            child1 = traverse(i+1, j)

        if j < n-1:
            child2 = traverse(i, j+1)

        return grid[i][j] + min(child1, child2)

    return traverse(0, 0)