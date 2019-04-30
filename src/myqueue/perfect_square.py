import queue
import math
import time

# BFS graph solution
class Solution(object):
    def numSquares(self, n):
        if n <= 0:
            return 0
        
        if n <= 1:
            return 1

        perfect_squares = []
        count_perfect_square = []
        ran = (x for x in range(1, n) if x * x <= n)
        for i in ran:
            perfect_squares.append(i*i)
            count_perfect_square.append(i*i)

        # Init graph
        myqueue = queue.Queue(maxsize=0)
        for i in perfect_squares:
            myqueue.put(i)

        if perfect_squares[-1] == n:
            return 1

        # Graph traversal
        counter = 1
        while not myqueue.empty():
            counter += 1

            myqueue_size = myqueue.qsize()
            for i in range(0, myqueue_size):
                tmp = myqueue.get()
                for j in perfect_squares:
                    if tmp + j == n:
                        return counter
                    elif tmp + j > n:
                        break
                    elif tmp + j < n and (tmp + j not in count_perfect_square):
                        myqueue.put(tmp + j)
                        count_perfect_square.append(tmp+j)
        return 
        
# Lagrange four-square theorem solution
# class Solution(object):
#     def numSquares(self, n):
#         return
