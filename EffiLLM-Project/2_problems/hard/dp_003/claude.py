class Solution:
    def dieSimulator(self, n, rollMax):
        MOD = 10**9 + 7
        
        # dp[i][j][k] = number of sequences of length i, ending with j consecutive face k+1
        dp = [[[0 for _ in range(6)] for _ in range(16)] for _ in range(n + 1)]
        
        # Base case: sequences of length 1
        for j in range(6):
            dp[1][1][j] = 1
        
        for i in range(2, n + 1):
            for j in range(6):  # Current face (0-indexed)
                for k in range(1, rollMax[j] + 1):  # Length of consecutive current face
                    if k == 1:  # Starting a new streak with face j+1
                        # Sum up all sequences ending with any other face
                        for prev_face in range(6):
                            if prev_face != j:
                                for prev_len in range(1, rollMax[prev_face] + 1):
                                    dp[i][1][j] = (dp[i][1][j] + dp[i-1][prev_len][prev_face]) % MOD
                    else:  # Extending a streak of face j+1
                        dp[i][k][j] = dp[i-1][k-1][j]
        
        # Sum up all possible sequences of length n
        result = 0
        for j in range(6):
            for k in range(1, rollMax[j] + 1):
                result = (result + dp[n][k][j]) % MOD
        
        return result