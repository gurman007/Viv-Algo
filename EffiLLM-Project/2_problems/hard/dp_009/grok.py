class Solution:
    def beautifulPartitions(self, s: str, k: int, minLength: int) -> int:
        MOD = 10**9 + 7
        n = len(s)
        primes = {'2', '3', '5', '7'}
        
        def is_valid_start(i):
            return s[i] in primes
            
        def is_valid_end(i):
            return s[i] not in primes
            
        dp = [[0] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 1
        
        for i in range(1, n + 1):
            for j in range(k + 1):
                dp[i][j] = dp[i - 1][j]
                if j > 0 and i >= minLength and is_valid_end(i - 1):
                    for m in range(i - minLength, -1, -1):
                        if is_valid_start(m):
                            dp[i][j] = (dp[i][j] + dp[m][j - 1]) % MOD
                            
        return dp[n][k]