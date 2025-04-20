from heapq import heappush, heappop

class Solution:
    def minimumVisitedCells(self, grid):
        m, n = len(grid), len(grid[0])
        # Using priority queue for Dijkstra's algorithm
        pq = [(1, 0, 0)]  # (steps, row, col)
        visited = set()
        
        while pq:
            steps, i, j = heappop(pq)
            
            # If we've reached the destination
            if i == m - 1 and j == n - 1:
                return steps
                
            # Skip if already visited
            if (i, j) in visited:
                continue
                
            visited.add((i, j))
            
            # Move right
            for k in range(j + 1, min(j + grid[i][j] + 1, n)):
                if (i, k) not in visited:
                    heappush(pq, (steps + 1, i, k))
                    
            # Move down
            for k in range(i + 1, min(i + grid[i][j] + 1, m)):
                if (k, j) not in visited:
                    heappush(pq, (steps + 1, k, j))
                    
        return -1