import queue


class Solution:

    def numIslands(self, grid):
        numIls = 0
        gridleny = len(grid)
        gridlenx = 0 if gridleny == 0 else len(grid[0])

        # Init grid visited 2d array

        grid_visited = []
        for i in range(0, gridleny):
            new_row = []
            for j in range(0, gridlenx):
                new_row.append(False)
            grid_visited.append(new_row)

        for i in range(0, gridleny):
            for j in range(0, gridlenx):
                if not grid_visited[i][j] and grid[i][j] == '1':
                    self.bfs(grid, grid_visited, i, j)
                    numIls += 1
        return numIls

    def bfs(self, grid, grid_visited, i, j):
        myqueue = queue.Queue()
        myqueue.put((i, j))

        gridleny = len(grid)
        gridlenx = len(grid[0])
        radiusy = 1
        radiusy = radiusy if (gridleny - radiusy > 0) else 0
        radiusx = 1
        radiusx = radiusx if (gridlenx - radiusx > 0) else 0
        
        while not myqueue.empty():
            y, x = myqueue.get()
            grid_visited[y][x] = True
            
            # Check neighbor

            for y0 in range(y - radiusy, y + radiusy + 1):
                for x0 in range(x - radiusx, x + radiusx + 1):
                    if self.is_neighbor(gridleny, gridlenx, radiusy, radiusx, y0, x0) \
                        and not self.is_diagonal_node(y0, x0, y, x) \
                        and not grid_visited[y0][x0] \
                        and grid[y0][x0] == '1':
                        myqueue.put((y0, x0))

    def is_neighbor(self, gridleny, gridlenx, radiusy, radiusx, y0, x0):
        return y0 >= 0 and x0 >= 0 and y0 < gridleny and x0 < gridlenx 

    def is_diagonal_node(self, y0, x0, y, x):
        return (y == y0 - 1 and x == x0 - 1) \ 
            or (y == y0 + 1 and x == x0 + 1) \
            or (y == y0 + 1 and x == x0 - 1) \
            or (y == y0 - 1 and x == x0 + 1)

grid = [
    ["1","1","1","1","1","0","1","1","1","1","1","1","1","1","1","0","1","0","1","1"],
    ["0","1","1","1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","1","0"],
    ["1","0","1","1","1","0","0","1","1","0","1","1","1","1","1","1","1","1","1","1"],
    ["1","1","1","1","0","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],
    ["1","0","0","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],
    ["1","0","1","1","1","1","1","1","0","1","1","1","0","1","1","1","0","1","1","1"],
    ["0","1","1","1","1","1","1","1","1","1","1","1","0","1","1","0","1","1","1","1"],
    ["1","1","1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","0","1","1"],
    ["1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","1","1","1","1","1"],
    ["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],
    ["0","1","1","1","1","1","1","1","0","1","1","1","1","1","1","1","1","1","1","1"],
    ["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],
    ["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],
    ["1","1","1","1","1","0","1","1","1","1","1","1","1","0","1","1","1","1","1","1"],
    ["1","0","1","1","1","1","1","0","1","1","1","0","1","1","1","1","0","1","1","1"],
    ["1","1","1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","1","1","0"],
    ["1","1","1","1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","0","0"],
    ["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],
    ["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],
    ["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"]
]

solution = Solution()
print(solution.numIslands(grid))