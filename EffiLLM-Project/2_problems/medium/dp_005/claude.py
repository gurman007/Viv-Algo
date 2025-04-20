class Solution:
    def maximumScoreAfterOperations(self, edges: list[list[int]], values: list[int]) -> int:
        n = len(values)
        graph = [[] for _ in range(n)]
        
        # Build adjacency list for the tree
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        # DFS function to compute the maximum score
        def dfs(node, parent):
            # If this is a leaf node
            if len(graph[node]) == 1 and graph[node][0] == parent:
                return 0, values[node]
            
            take_sum = 0
            leave_sum = values[node]
            
            # Process all children
            for child in graph[node]:
                if child != parent:
                    take_child, leave_child = dfs(child, node)
                    # If we take current node, we can choose best option for each child
                    take_sum += max(take_child, leave_child)
                    # If we leave current node, we must ensure path sum is not zero
                    # So we must take at least one node in each subtree
                    leave_sum += take_child
            
            return take_sum, leave_sum
        
        # For root node (node 0), we compare two strategies
        take_root, leave_root = dfs(0, -1)
        return max(take_root, leave_root)