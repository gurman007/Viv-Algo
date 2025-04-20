from typing import List
from collections import Counter

class Solution:
    def squareFreeSubsets(self, nums: List[int]) -> int:
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        mod = 10**9 + 7
        cnt = Counter(nums)
        f = [0] * (1 << len(primes))
        f[0] = pow(2, cnt[1], mod)

        for x in range(2, 31):
            if cnt[x] == 0 or x % 4 == 0 or x % 9 == 0 or x % 25 == 0:
                continue
            mask = 0
            for i, p in enumerate(primes):
                if x % p == 0:
                    mask |= 1 << i
            for state in range((1 << len(primes)) - 1, -1, -1):
                if state & mask == 0:
                    f[state | mask] = (f[state | mask] + f[state] * cnt[x]) % mod

        return (sum(f) - 1) % mod
