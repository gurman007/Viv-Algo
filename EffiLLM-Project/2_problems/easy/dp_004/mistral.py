# Generated by Mistral 7B via Ollama

class Solution:
    def generate(self, numRows):
        if not numRows: return []
        triangle = [[1]]
        for i in range(1, numRows):
            row = [triangle[i-1][j]+triangle[i-1][j+1] if 0 < j < len(triangle[i-1]) else 1 for j in range(i+1)]
            triangle.append(row)
        return triangle

