class Solution:
    def beautifulPartitions(self, s: str, k: int, minLength: int) -> int:
        MOD = 10**9 + 7
        n = len(s)
        
        # Helper functions to identify prime and non-prime digits
        def is_prime(c):
            return c in {'2', '3', '5', '7'}
        
        def is_non_prime(c):
            return c in {'1', '4', '6', '8', '9'}
        
        # The first character must be prime and the last must be non-prime
        if not is_prime(s[0]) or not is_non_prime(s[n-1]):
            return 0
        
        # Find all potential partition positions
        # A position i is valid if s[i-1] is non-prime and s[i] is prime
        valid_positions = [0]  # Starting position is always valid
        for i in range(1, n):
            if is_non_prime(s[i-1]) and is_prime(s[i]):
                valid_positions.append(i)
        
        # Add the end position
        valid_positions.append(n)
        
        m = len(valid_positions)
        
        # dp[i][j] = number of ways to make j partitions using the first i valid positions
        dp = [[0] * (k + 1) for _ in range(m)]
        
        # Base case: one way to make 0 partitions using 0 positions
        dp[0][0] = 1
        
        for i in range(1, m):
            curr_pos = valid_positions[i]
            
            for j in range(i):
                prev_pos = valid_positions[j]
                
                # Check if the substring length meets the minimum requirement
                if curr_pos - prev_pos >= minLength:
                    for p in range(1, k + 1):
                        dp[i][p] = (dp[i][p] + dp[j][p-1]) % MOD
        
        return dp[m-1][k]