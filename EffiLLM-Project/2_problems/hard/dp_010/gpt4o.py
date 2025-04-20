from typing import List

class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        n, m = len(nums1), len(nums2)
        dp = [[float('-inf')] * (m + 1) for _ in range(n + 1)]
        for i in range(n):
            for j in range(m):
                prod = nums1[i] * nums2[j]
                dp[i + 1][j + 1] = max(
                    dp[i][j] + prod,
                    prod,
                    dp[i][j + 1],
                    dp[i + 1][j]
                )
        return dp[n][m]
