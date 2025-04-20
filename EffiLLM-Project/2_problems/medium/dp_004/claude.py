from typing import List

class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        n = len(arr)
        
        # dp[i][j] = minimum sum of non-leaf nodes in the subtree spanning arr[i...j]
        dp = [[float('inf')] * n for _ in range(n)]
        
        # max_val[i][j] = maximum leaf value in the subarray arr[i...j]
        max_val = [[0] * n for _ in range(n)]
        
        # Initialize max_val for single elements
        for i in range(n):
            dp[i][i] = 0  # No non-leaf nodes in a single leaf
            max_val[i][i] = arr[i]
        
        # Compute max_val for all subarrays
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                max_val[i][j] = max(max_val[i][j-1], max_val[i+1][j], arr[i], arr[j])
        
        # Fill dp table bottom-up
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                
                # Try all possible roots (split points)
                for k in range(i, j):
                    dp[i][j] = min(dp[i][j], 
                                  dp[i][k] + dp[k+1][j] + max_val[i][k] * max_val[k+1][j])
        
        return dp[0][n-1]