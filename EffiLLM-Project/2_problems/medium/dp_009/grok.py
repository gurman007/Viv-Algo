class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)
        s = s + s
        alt1, alt2 = "01" * n, "10" * n
        
        diff1 = diff2 = 0
        for i in range(n):
            diff1 += s[i] != alt1[i]
            diff2 += s[i] != alt2[i]
            
        min_flips = min(diff1, diff2)
        
        for i in range(n, 2 * n - 1):
            diff1 -= s[i - n] != alt1[i - n]
            diff2 -= s[i - n] != alt2[i - n]
            diff1 += s[i] != alt1[i]
            diff2 += s[i] != alt2[i]
            min_flips = min(min_flips, diff1, diff2)
            
        return min_flips