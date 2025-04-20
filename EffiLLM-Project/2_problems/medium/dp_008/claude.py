from collections import deque

class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        if amount == 0:
            return 0
        
        # Initialize DP array with amount+1 (as maximum possible answer)
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        
        # Fill the dp array
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i], dp[i - coin] + 1)
        
        # Return -1 if no solution exists
        return dp[amount] if dp[amount] != float('inf') else -1