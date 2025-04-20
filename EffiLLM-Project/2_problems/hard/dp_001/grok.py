from collections import deque

class Solution:
    def minimumVisitedCells(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        queue = deque([(0, 0, 1)])
        visited = {(0, 0)}
        
        while queue:
            i, j, steps = queue.popleft()
            
            if i == m - 1 and j == n - 1:
                return steps
                
            jump = grid[i][j]
            
            for nj in range(j + 1, min(n, j + jump + 1)):
                if (i, nj) not in visited:
                    visited.add((i, nj))
                    queue.append((i, nj, steps + 1))
                    
            for ni in range(i + 1, min(m, i + jump + 1)):
                if (ni, j) not in visited:
                    visited.add((ni, j))
                    queue.append((ni, j, steps + 1))
                    
        return -1