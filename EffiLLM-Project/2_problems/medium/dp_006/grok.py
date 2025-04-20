class Solution:
    def squareFreeSubsets(self, nums: list[int]) -> int:
        MOD = 10**9 + 7
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        n = len(primes)
        
        def get_mask(num):
            mask = 0
            for i, p in enumerate(primes):
                if num % (p * p) == 0:
                    return -1
                if num % p == 0:
                    mask |= 1 << i
            return mask
        
        dp = [0] * (1 << n)
        dp[0] = 1
        
        for num in nums:
            mask = get_mask(num)
            if mask != -1:
                for prev in range((1 << n) - 1, -1, -1):
                    if prev & mask == 0:
                        dp[prev | mask] = (dp[prev | mask] + dp[prev]) % MOD
        
        return (sum(dp) - 1) % MOD