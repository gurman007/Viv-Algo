class Solution:
    def uniqueLetterString(self, s: str) -> int:
        n = len(s)
        last_positions = {}
        result = 0
        
        # Store the last two positions of each character
        for i in range(n):
            char = s[i]
            if char not in last_positions:
                last_positions[char] = [-1, -1]
            last_positions[char][0], last_positions[char][1] = last_positions[char][1], i
        
        # Calculate the contribution of each character to all substrings
        for char, positions in last_positions.items():
            positions.append(n)  # Add a boundary position at the end
            for i in range(1, len(positions) - 1):
                result += (positions[i] - positions[i-1]) * (positions[i+1] - positions[i])
        
        return result