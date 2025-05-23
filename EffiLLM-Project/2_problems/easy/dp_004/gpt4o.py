from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        for _ in range(1, numRows):
            row = [1]
            for i in range(1, len(res[-1])):
                row.append(res[-1][i - 1] + res[-1][i])
            row.append(1)
            res.append(row)
        return res
