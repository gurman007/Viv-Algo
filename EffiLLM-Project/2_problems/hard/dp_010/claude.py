from typing import List

class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)
        
        # dp[i][j] represents the maximum dot product of subseq of nums1[0...i-1] and nums2[0...j-1]
        dp = [[float('-inf')] * (n + 1) for _ in range(m + 1)]
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # Include current elements in the dot product
                dp[i][j] = max(
                    dp[i-1][j-1] + nums1[i-1] * nums2[j-1],  # Current pair and previous result
                    dp[i-1][j],                              # Skip element from nums1
                    dp[i][j-1],                              # Skip element from nums2
                    nums1[i-1] * nums2[j-1]                  # Start a new subsequence with current elements
                )
        
        return dp[m][n]