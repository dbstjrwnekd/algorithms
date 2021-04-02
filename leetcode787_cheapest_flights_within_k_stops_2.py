import collections

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        if src == dst:
            return 0
        
        graph = collections.defaultdict(list)
        
        for u, v, w in flights:
            graph[u].append((v,w))
        
        Q = [(0,src,K)]
        
        while Q:
            time, node, count = heapq.heappop(Q)
            if node == dst:
                return time
            
            if count >= 0:
                for v, w in graph[node]:
                    heapq.heappush(Q, (time+w, v, count-1))
        
        return -1
        