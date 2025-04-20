class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)
        s += s
        alt1 = ''.join(['0' if i % 2 == 0 else '1' for i in range(2 * n)])
        alt2 = ''.join(['1' if i % 2 == 0 else '0' for i in range(2 * n)])
        res = float('inf')
        diff1 = diff2 = 0

        for i in range(2 * n):
            if s[i] != alt1[i]:
                diff1 += 1
            if s[i] != alt2[i]:
                diff2 += 1
            if i >= n:
                if s[i - n] != alt1[i - n]:
                    diff1 -= 1
                if s[i - n] != alt2[i - n]:
                    diff2 -= 1
            if i >= n - 1:
                res = min(res, diff1, diff2)
        return res
