class Solution:
    def maxProfit(self, k: int, prices: list[int]) -> int:
        if not prices or k == 0:
            return 0
            
        n = len(prices)
        if k >= n // 2:
            profit = 0
            for i in range(1, n):
                if prices[i] > prices[i-1]:
                    profit += prices[i] - prices[i-1]
            return profit
            
        dp = [[[0] * 2 for _ in range(k + 1)] for _ in range(n)]
        
        for i in range(n):
            for j in range(k + 1):
                if i == 0:
                    dp[0][j][0] = 0
                    dp[0][j][1] = -prices[0]
                    continue
                    
                dp[i][j][0] = dp[i-1][j][0]
                if j > 0:
                    dp[i][j][0] = max(dp[i][j][0], dp[i-1][j-1][1] + prices[i])
                    
                dp[i][j][1] = dp[i-1][j][1]
                dp[i][j][1] = max(dp[i][j][1], dp[i-1][j][0] - prices[i])
                
        return dp[n-1][k][0]