class Solution:
    def divisorGame(self, n):
        # Alice wins if n is even
        return n % 2 == 0