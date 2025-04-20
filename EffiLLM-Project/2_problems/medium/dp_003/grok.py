class Solution:
    def subarrayBitwiseORs(self, arr: list[int]) -> int:
        result = set()
        curr = {0}
        
        for num in arr:
            next_set = {num}
            for prev in curr:
                next_set.add(prev | num)
            curr = next_set
            result.update(curr)
            
        return len(result)