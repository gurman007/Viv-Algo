class Solution:
    def maxAlternatingSum(self, nums: list[int]) -> int:
        even = odd = 0
        
        for num in nums:
            next_even = max(even, odd + num)
            next_odd = max(odd, even - num)
            even, odd = next_even, next_odd
            
        return even