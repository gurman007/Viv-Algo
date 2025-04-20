from typing import List

class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        mod = 10**9 + 7
        dp = [[0] * 6 for _ in range(n + 1)]
        cnt = [[0] * 6 for _ in range(n + 1)]
        for i in range(6):
            dp[1][i] = 1
            cnt[1][i] = 1
        for i in range(2, n + 1):
            for j in range(6):
                for k in range(6):
                    if j == k:
                        if cnt[i - 1][k] < rollMax[k]:
                            dp[i][j] = (dp[i][j] + dp[i - 1][k]) % mod
                            cnt[i][j] = cnt[i - 1][k] + 1
                    else:
                        dp[i][j] = (dp[i][j] + dp[i - 1][k]) % mod
                        cnt[i][j] = 1
        return sum(dp[n]) % mod
