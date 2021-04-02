import collections

class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        dist = [float('inf')] * N
        graph = collections.defaultdict(list)
        check = [False] * N
        
        for u, v, w in times:
            graph[u].append((v,w))
        
        dist[K-1] = 0
        check[K-1] = True
        self.dijkstra(graph, dist, N, K, check)
        
        answer = max(dist)
        
        if answer == float('inf'):
            answer = -1
        
        return answer
    
    def dijkstra(self, graph, dist, N, K, check):
        step = K
        for i in range(N):
            self.update_dist(dist, graph, step)
            step = self.get_next_step(dist, check)
            if step == None:
                return
            step += 1
            check[step-1] = True
            
    def update_dist(self, dist, graph, K):
        if K in graph:
            for v, w in graph[K]:
                if dist[K-1] + w < dist[v-1]:
                    dist[v-1] = dist[K-1] + w
    
    def get_next_step(self, dist, check):
        next_node, min_dist = None, float('inf')
        for node in range(len(dist)):
            if not check[node] and dist[node] < min_dist:
                min_dist = dist[node]
                next_node = node
        return next_node
        
        