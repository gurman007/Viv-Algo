class Solution:
    def sellingWood(self, m: int, n: int, prices: list[list[int]]) -> int:
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        for h, w, price in prices:
            dp[h][w] = price
            
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                for k in range(1, i):
                    dp[i][j] = max(dp[i][j], dp[k][j] + dp[i - k][j])
                for k in range(1, j):
                    dp[i][j] = max(dp[i][j], dp[i][k] + dp[i][j - k])
                    
        return dp[m][n]