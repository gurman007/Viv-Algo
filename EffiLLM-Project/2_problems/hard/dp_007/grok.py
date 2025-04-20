class Solution:
    def uniqueLetterString(self, s: str) -> int:
        MOD = 10**9 + 7
        n = len(s)
        last = {}
        dp = [0] * (n + 1)
        last_pos = [-1] * 26
        
        for i in range(n):
            c = ord(s[i]) - ord('A')
            dp[i + 1] = (2 * dp[i] - dp[last_pos[c]] + i - last_pos[c]) % MOD
            last_pos[c] = i
            
        return dp[n]