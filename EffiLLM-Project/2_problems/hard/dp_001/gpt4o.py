from typing import List
from collections import deque
from sortedcontainers import SortedList

class Solution:
    def minimumVisitedCells(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        row = [SortedList(range(n)) for _ in range(m)]
        col = [SortedList(range(m)) for _ in range(n)]
        q = deque([(0, 0, 1)])
        row[0].remove(0)
        col[0].remove(0)
        while q:
            i, j, d = q.popleft()
            if i == m - 1 and j == n - 1:
                return d
            for k in list(row[i].irange(j + 1, j + grid[i][j])):
                q.append((i, k, d + 1))
                row[i].remove(k)
                col[k].remove(i)
            for k in list(col[j].irange(i + 1, i + grid[i][j])):
                q.append((k, j, d + 1))
                col[j].remove(k)
                row[k].remove(j)
        return -1
