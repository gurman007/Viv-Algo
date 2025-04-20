from typing import List

class Solution:
    def cheapestJump(self, coins: List[int], maxJump: int) -> List[int]:
        n = len(coins)
        if n == 0 or coins[n-1] == -1:  # Cannot reach the end
            return []
        
        # Initialize dp array with infinity and path array
        dp = [float('inf')] * n
        dp[0] = coins[0]
        
        # next[i] stores the next position to jump to from i
        next_jump = [-1] * n
        
        for i in range(n):
            if coins[i] == -1:
                continue
                
            for j in range(1, maxJump + 1):
                if i + j < n and coins[i + j] != -1:
                    new_cost = dp[i] + coins[i + j]
                    
                    if new_cost < dp[i + j]:
                        dp[i + j] = new_cost
                        next_jump[i + j] = i
        
        # If we cannot reach the end
        if dp[n-1] == float('inf'):
            return []
        
        # Reconstruct the path
        path = []
        pos = n - 1
        
        while pos != -1:
            path.append(pos + 1)  # 1-indexed
            pos = next_jump[pos]
        
        return path[::-1]  # Reverse to get the path from start to end