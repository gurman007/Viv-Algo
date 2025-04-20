from collections import defaultdict

class Solution:
    def maximumScoreAfterOperations(self, edges: list[list[int]], values: list[int]) -> int:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        def dfs(node: int, parent: int) -> tuple[int, int]:
            keep = values[node]
            lose = 0
            total_child_sum = 0
            
            for child in graph[node]:
                if child != parent:
                    child_keep, child_lose = dfs(child, node)
                    keep += child_lose
                    lose += max(child_keep, child_lose)
                    total_child_sum += child_keep
            
            if not total_child_sum:
                keep = 0
                
            return keep, lose
        
        return max(dfs(0, -1)[1], dfs(0, -1)[0])