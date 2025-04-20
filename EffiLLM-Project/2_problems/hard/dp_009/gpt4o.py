from typing import List
from functools import lru_cache

class Solution:
    def beautifulPartitions(self, s: str, k: int, minLength: int) -> int:
        mod = 10**9 + 7
        n = len(s)
        primes = {'2', '3', '5', '7'}

        if s[0] not in primes or s[-1] in primes:
            return 0

        @lru_cache(None)
        def dp(i: int, cuts: int) -> int:
            if cuts == 0:
                return int(i == n)
            if i >= n:
                return 0
            res = 0
            if s[i] in primes:
                for j in range(i + minLength - 1, n - (cuts - 1) * minLength):
                    if s[j] not in primes:
                        res = (res + dp(j + 1, cuts - 1)) % mod
            return res

        return dp(0, k)
