import collections
import heapq

def solution(N, road, K):
    answer = 0
    graph = collections.defaultdict(list)
    
    for u, v, w in road:
        graph[u].append((v,w))
        graph[v].append((u,w))
        
    dist = collections.defaultdict(int)
    Q = [(0,1)]
    
    while Q:
        time, node = heapq.heappop(Q)
        if node not in dist:
            dist[node] = time
        
        for v, w in graph[node]:
            if not v in dist and time + w <= K:
                heapq.heappush(Q, (time+w, v))
    
    return len(dist)