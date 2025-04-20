from typing import List

class Solution:
    def cheapestJump(self, coins: List[int], maxJump: int) -> List[int]:
        n = len(coins)
        dp = [float('inf')] * n
        path = [[] for _ in range(n)]
        if coins[0] == -1:
            return []
        dp[0] = coins[0]
        path[0] = [1]
        for i in range(1, n):
            if coins[i] == -1:
                continue
            for j in range(max(0, i - maxJump), i):
                if dp[j] + coins[i] < dp[i] or (dp[j] + coins[i] == dp[i] and path[j] + [i + 1] < path[i]):
                    dp[i] = dp[j] + coins[i]
                    path[i] = path[j] + [i + 1]
        return path[-1]
