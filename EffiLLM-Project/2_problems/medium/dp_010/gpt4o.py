from typing import List

class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        even, odd = 0, 0
        for num in nums:
            even, odd = max(even, odd + num), even - num
        return even
