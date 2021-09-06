import collections

class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        graph = collections.defaultdict(list)
        for start, end, length in times:
            graph[start].append((end, length))
        
        dist = collections.defaultdict(int)
        
        queue = [(0,K)]
        
        while queue:
            length, node = heapq.heappop(queue)
            if node not in dist:
                dist[node] = length
                for v, w in graph[node]:
                    heapq.heappush(queue,(length+w, v))

        if len(dist) < N:
            return -1
        
        return max(dist.values())
        