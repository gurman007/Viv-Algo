class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        MOD = 10**9 + 7
        
        # We can only go as far as steps/2 positions to the right
        # because we need to come back to position 0
        max_position = min(steps // 2 + 1, arrLen)
        
        # dp[i][j] represents the number of ways to reach position j after i steps
        dp = [[0] * max_position for _ in range(steps + 1)]
        dp[0][0] = 1  # Start at position 0
        
        for i in range(1, steps + 1):
            for j in range(max_position):
                # Stay at the same position
                dp[i][j] = dp[i-1][j]
                
                # Move from left
                if j > 0:
                    dp[i][j] = (dp[i][j] + dp[i-1][j-1]) % MOD
                
                # Move from right
                if j < max_position - 1:
                    dp[i][j] = (dp[i][j] + dp[i-1][j+1]) % MOD
        
        return dp[steps][0]