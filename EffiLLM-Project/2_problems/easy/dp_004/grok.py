class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        triangle = [[1]]
        for i in range(1, numRows):
            prev = triangle[-1]
            new_row = [1] * (i + 1)
            for j in range(1, i):
                new_row[j] = prev[j-1] + prev[j]
            triangle.append(new_row)
        return triangle