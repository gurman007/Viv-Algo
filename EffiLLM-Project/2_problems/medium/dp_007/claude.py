from collections import deque

class Solution:
    def maxResult(self, nums: list[int], k: int) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        
        # Use deque to maintain a monotonically decreasing queue of indices
    
        dq = deque([0])  # Start with index 0
        
        # dp[i] represents the maximum score to reach index i
        dp = [0] * n
        dp[0] = nums[0]
        
        for i in range(1, n):
            # Get the maximum score from the previous indices
            # The front of deque contains the index with maximum score
            dp[i] = dp[dq[0]] + nums[i]
            
            # Remove indices that are out of the window [i-k, i-1]
            while dq and dq[0] < i - k:
                dq.popleft()
            
            # Remove indices with smaller scores from the back
            while dq and dp[dq[-1]] <= dp[i]:
                dq.pop()
            
            # Add current index to deque
            dq.append(i)
        
        return dp[n-1]