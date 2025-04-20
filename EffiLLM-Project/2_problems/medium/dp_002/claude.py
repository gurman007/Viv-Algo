class Solution:
    def soupServings(self, n: int) -> float:
        # For large n, the probability approaches 1
        if n >= 5000:
            return 1.0
        
        # Convert n to number of servings (each serving is 25ml)
        n = (n + 24) // 25
        
        # Memoization
        memo = {}
        
        def dp(a, b):
            if (a, b) in memo:
                return memo[(a, b)]
            
            # Base cases
            if a <= 0 and b <= 0:
                return 0.5
            if a <= 0:
                return 1.0
            if b <= 0:
                return 0.0
            
            # Calculate probability for each operation
            result = 0.25 * (
                dp(a - 4, b) +          # Serve 100ml of A, 0ml of B
                dp(a - 3, b - 1) +      # Serve 75ml of A, 25ml of B
                dp(a - 2, b - 2) +      # Serve 50ml of A, 50ml of B
                dp(a - 1, b - 3)        # Serve 25ml of A, 75ml of B
            )
            
            memo[(a, b)] = result
            return result
        
        return dp(n, n)