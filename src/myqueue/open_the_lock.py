import time

class Solution(object):
    def openLock(self, deadends, target):
        moved, q, cnt, move = set(deadends), ['0000'], 0, {str(
            i): [str((i+1) % 10), str((i-1) % 10)] for i in range(10)}
        if '0000' in moved:
            return -1 
        while q:
            new = []
            cnt += 1
            for code in q:
                for i, c in enumerate(code):
                    for curr in [code[:i] + move[c][0] + code[i+1:], code[:i] + move[c][1] + code[i+1:]]:
                        if curr not in moved:
                            if curr == target:
                                return cnt
                            new.append(curr)
                            # node visited
                            moved.add(curr)
            q = new
        return -1
