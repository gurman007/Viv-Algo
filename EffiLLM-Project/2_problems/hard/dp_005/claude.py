from typing import List

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        if n <= 1 or k == 0:
            return 0
        
        # If k is large enough, we can make as many transactions as we want
        if k >= n // 2:
            max_profit = 0
            for i in range(1, n):
                if prices[i] > prices[i-1]:
                    max_profit += prices[i] - prices[i-1]
            return max_profit
        
        # dp[i][j] represents the maximum profit with at most i transactions on day j
        dp = [[0 for _ in range(n)] for _ in range(k+1)]
        
        for i in range(1, k+1):
            max_diff = -prices[0]  # Initialize max difference
            for j in range(1, n):
                # Either we don't make a transaction on day j, or we sell on day j
                dp[i][j] = max(dp[i][j-1], prices[j] + max_diff)
                
                # Update max_diff for the next iteration
                max_diff = max(max_diff, dp[i-1][j] - prices[j])
        
        return dp[k][n-1]