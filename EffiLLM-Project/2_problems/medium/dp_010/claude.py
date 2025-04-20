class Solution:
    def maxAlternatingSum(self, nums: list[int]) -> int:
        # Initialize two variables to track the maximum alternating sum
        # even: maximum sum ending with an element at even position
        # odd: maximum sum ending with an element at odd position
        even = 0
        odd = 0
        
        for num in nums:
            # For each number, we have two choices:
            # 1. Include it in our subsequence
            # 2. Skip it
            
            # If we include this number at an even position, we can:
            # - Either add it to the previous odd position sum
            # - Or start a new subsequence with just this number
            new_even = max(odd + num, even, num)
            
            # If we include this number at an odd position, we can:
            # - Subtract it from the previous even position sum
            new_odd = max(even - num, odd)
            
            even, odd = new_even, new_odd
        
        # The maximum alternating sum will always end at an even position
        # (because we want to maximize the sum)
        return even