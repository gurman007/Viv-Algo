class Solution:
    def dieSimulator(self, n: int, rollMax: list[int]) -> int:
        MOD = 10**9 + 7
        dp = [[0] * 6 for _ in range(n + 1)]
        dp[0][0] = 1
        
        for i in range(1, n + 1):
            for j in range(6):
                for k in range(1, min(i + 1, rollMax[j] + 1)):
                    if i - k >= 0:
                        for prev in range(6):
                            if prev != j:
                                dp[i][j] = (dp[i][j] + dp[i - k][prev]) % MOD
                    else:
                        dp[i][j] = (dp[i][j] + 1) % MOD
        
        return sum(dp[n]) % MOD