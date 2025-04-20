from typing import List

class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        result = set()
        current = set()
        
        for num in arr:
            current = {num | prev for prev in current} | {num}
            result.update(current)
        
        return len(result)