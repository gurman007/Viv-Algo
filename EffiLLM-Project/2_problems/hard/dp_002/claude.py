class Solution:
    def maxEnvelopes(self, envelopes):
        if not envelopes:
            return 0
        
        # Sort by width ascending, and if width is the same, by height descending
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        
        # Find the longest increasing subsequence based on heights
        heights = [env[1] for env in envelopes]
        
        # dp[i] = smallest height at which subsequence of length i ends
        dp = []
        
        for height in heights:
            # Binary search to find the position to insert the current height
            left, right = 0, len(dp)
            while left < right:
                mid = (left + right) // 2
                if dp[mid] < height:
                    left = mid + 1
                else:
                    right = mid
            
            if left == len(dp):
                dp.append(height)
            else:
                dp[left] = height
        
        return len(dp)