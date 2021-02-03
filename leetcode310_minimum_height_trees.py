import collections

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 1:
            return [0]
        
        adj = collections.defaultdict(list)
        
        for i, j in edges:
            adj[i].append(j)
            adj[j].append(i)
            
        leaves = []
        
        for i in range(n):
            if len(adj[i]) == 1:
                leaves.append(i)
        
        while n > 2:
            n -= len(leaves)
            new_leaves = []
            
            for leaf in leaves:
                neighbor = adj[leaf].pop()
                adj[neighbor].remove(leaf)
                
                if len(adj[neighbor]) == 1:
                    new_leaves.append(neighbor)
                
            leaves = new_leaves
        
        return leaves