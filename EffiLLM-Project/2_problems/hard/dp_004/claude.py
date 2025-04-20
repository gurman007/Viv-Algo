from typing import List

class Solution:
    def sellingWood(self, m: int, n: int, prices: List[List[int]]) -> int:
        # Create a dictionary of prices for fast lookup
        price_map = {(h, w): p for h, w, p in prices}
        
        # Create a DP table where dp[i][j] represents the maximum profit
        # that can be obtained from a piece of wood of size i x j
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # Fill in the values from the prices list
        for h, w, p in prices:
            if h <= m and w <= n:
                dp[h][w] = p
        
        # Calculate maximum profit for each possible size
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # Try horizontal cuts
                for k in range(1, i):
                    dp[i][j] = max(dp[i][j], dp[k][j] + dp[i - k][j])
                
                # Try vertical cuts
                for k in range(1, j):
                    dp[i][j] = max(dp[i][j], dp[i][k] + dp[i][j - k])
        
        return dp[m][n]