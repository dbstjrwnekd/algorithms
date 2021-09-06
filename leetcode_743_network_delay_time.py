import collections

class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        graph = collections.defaultdict(list)
        for start, end, length in times:
            graph[start].append((end, length))
        
        s = set()
        visit_length = [float('inf')] * N
        max_length = 0
        
        def dijkstra():
            cur = K
            visit_length[cur-1] = 0
            while True:
                s.add(cur)
                updateLength(cur)
                cur = getNextNode()
                if not cur:
                    break
                    
        def updateLength(cur):
            for next_node, length in graph[cur]:
                visit_length[next_node-1] = min(visit_length[next_node-1], visit_length[cur-1] + length)
        
        def getNextNode():
            cur = None
            min_length = float('inf')
            for node in range(1,N+1):
                if node not in s and visit_length[node-1] < min_length:
                        cur = node
                        min_length = visit_length[node-1]
            return cur
                
        dijkstra()
        
        if float('inf') in visit_length:
            return -1
            
        return max(visit_length)
        