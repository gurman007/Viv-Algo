class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)
        
        # Double the string for simulating rotation
        s = s + s
        
        # Create two alternating patterns
        alt1 = ""  # Starts with '0'
        alt2 = ""  # Starts with '1'
        
        for i in range(len(s)):
            alt1 += '0' if i % 2 == 0 else '1'
            alt2 += '1' if i % 2 == 0 else '0'
        
        # Initialize results
        res = float('inf')
        diff1 = 0  # Differences with alt1
        diff2 = 0  # Differences with alt2
        
        # Sliding window of size n
        for i in range(len(s)):
            # Add new character differences
            if s[i] != alt1[i]:
                diff1 += 1
            if s[i] != alt2[i]:
                diff2 += 1
                
            # Remove the leftmost character if window exceeds size n
            if i >= n:
                if s[i - n] != alt1[i - n]:
                    diff1 -= 1
                if s[i - n] != alt2[i - n]:
                    diff2 -= 1
            
            # Update result when we have a full window
            if i >= n - 1:
                res = min(res, min(diff1, diff2))
        
        return res