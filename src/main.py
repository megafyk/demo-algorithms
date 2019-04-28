import queue

class Solution:
    
    def numIslands(self, grid) -> int:
        numIls = 0
        gridlen = len(grid)

        # Init grid visited 2d array
        grid_visited = []
        for i in range(0, gridlen):
            new_row = []
            for j in range(0, gridlen):
                new_row.append(False)
            grid_visited.append(new_row)

        

        # Find first root node
        for i in range(0, gridlen):
            for j in range(0, gridlen):
                #bfs + numIls+=1 
                    
        return numIls

    @staticmethod
    def bfs(grid, grid_visited, i, j):
        myqueue = queue.Queue(maxsize=0)
        queue.put([i, j])
        grid_len = len(grid)
        while not myqueue.empty():
            arr = queue.get()
            x = arr[0]
            y = arr[1]
            #check neighbor
            

            
            


    @staticmethod
    def is_neighbor(gridlen, i, j):
        return i >= 0 and i < gridlen and j >= 0 and j < gridlen
