from typing import List

class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        mod = 10**9 + 7
        max_pos = min(steps // 2 + 1, arrLen)
        dp = [0] * max_pos
        dp[0] = 1
        for _ in range(steps):
            dp_new = [0] * max_pos
            for i in range(max_pos):
                dp_new[i] = dp[i]
                if i > 0:
                    dp_new[i] = (dp_new[i] + dp[i - 1]) % mod
                if i + 1 < max_pos:
                    dp_new[i] = (dp_new[i] + dp[i + 1]) % mod
            dp = dp_new
        return dp[0]
