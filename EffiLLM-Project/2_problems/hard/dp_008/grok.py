class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        MOD = 10**9 + 7
        max_pos = min(steps // 2 + 1, arrLen)
        dp = [0] * max_pos
        dp[0] = 1
        
        for _ in range(steps):
            next_dp = [0] * max_pos
            for j in range(max_pos):
                next_dp[j] = (next_dp[j] + dp[j]) % MOD
                if j > 0:
                    next_dp[j - 1] = (next_dp[j - 1] + dp[j]) % MOD
                if j < max_pos - 1:
                    next_dp[j + 1] = (next_dp[j + 1] + dp[j]) % MOD
            dp = next_dp
            
        return dp[0]