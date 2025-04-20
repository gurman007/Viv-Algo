class Solution:
    def mctFromLeafValues(self, arr: list[int]) -> int:
        stack = []
        total = 0
        
        for num in arr:
            while stack and stack[-1] <= num:
                mid = stack.pop()
                if stack:
                    total += mid * min(stack[-1], num)
                else:
                    total += mid * num
            stack.append(num)
        
        while len(stack) > 1:
            total += stack.pop() * stack[-1]
        
        return total