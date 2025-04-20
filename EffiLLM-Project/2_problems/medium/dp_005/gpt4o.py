from typing import List
from collections import defaultdict

class Solution:
    def maximumScoreAfterOperations(self, edges: List[List[int]], values: List[int]) -> int:
        tree = defaultdict(list)
        for a, b in edges:
            tree[a].append(b)
            tree[b].append(a)

        def dfs(node, parent):
            total = 0
            for child in tree[node]:
                if child != parent:
                    total += dfs(child, node)
            return min(values[node], total) if total else values[node]

        return sum(values) - dfs(0, -1)
