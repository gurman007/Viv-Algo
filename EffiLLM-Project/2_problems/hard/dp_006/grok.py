from collections import deque
import heapq

class Solution:
    def cheapestJump(self, coins: list[int], maxJump: int) -> list[int]:
        n = len(coins)
        if coins[n-1] == -1:
            return []
            
        dp = [float('inf')] * n
        dp[0] = coins[0]
        prev = [-1] * n
        queue = deque([(0, coins[0], [1])])
        
        while queue:
            i, cost, path = queue.popleft()
            
            if cost > dp[i]:
                continue
                
            for k in range(1, maxJump + 1):
                j = i + k
                if j < n and coins[j] != -1:
                    new_cost = cost + coins[j]
                    if new_cost <= dp[j]:
                        if new_cost < dp[j] or path + [j + 1] < prev[j]:
                            dp[j] = new_cost
                            prev[j] = path + [j + 1]
                            queue.append((j, new_cost, path + [j + 1]))
        
        return prev[n-1] if dp[n-1] != float('inf') else []