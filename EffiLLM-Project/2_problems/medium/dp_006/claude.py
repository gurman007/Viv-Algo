class Solution:
    def squareFreeSubsets(self, nums: list[int]) -> int:
        MOD = 10**9 + 7
        
        # First 10 primes
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        
        # Count frequencies of each number in nums
        freq = {}
        for num in nums:
            # Skip numbers divisible by square numbers
            is_square_free = True
            for p in primes:
                if p * p <= num and num % (p * p) == 0:
                    is_square_free = False
                    break
            if is_square_free:
                freq[num] = freq.get(num, 0) + 1
        
        # Get unique square-free numbers
        unique_nums = list(freq.keys())
        n = len(unique_nums)
        
        # Map each number to its prime signature (bitmask)
        def get_mask(num):
            mask = 0
            for i, p in enumerate(primes):
                if num % p == 0:
                    mask |= (1 << i)
            return mask
        
        # Compute masks for each unique number
        masks = [get_mask(num) for num in unique_nums]
        
        # DP[mask] = number of ways to get prime signature mask
        dp = [0] * (1 << len(primes))
        dp[0] = 1  # Empty set
        
        # Compute dp
        for i in range(n):
            num = unique_nums[i]
            mask = masks[i]
            
            # Special case for 1 (can use any number of 1s)
            if num == 1:
                # Adding any number of 1s doesn't change the prime signature
                dp[0] = pow(2, freq[1], MOD)
                continue
            
            # For other numbers, we either use it or don't
            for j in range((1 << len(primes)) - 1, -1, -1):
                # Skip if j and mask share any prime factors
                if j & mask:
                    continue
                
                # Add frequency of current number to dp[j|mask]
                dp[j | mask] = (dp[j | mask] + dp[j] * freq[num]) % MOD
        
        # Sum all non-empty subsets
        return (sum(dp) - 1) % MOD