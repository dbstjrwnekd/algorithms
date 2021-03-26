def solution(N, road, K):
    answer = 0
    dist = [float('inf')] * N
    dist[0] = 0
    visited = [False] * N
    visited[0] = True
    graph = [[0] * N for _ in range(N)]
    
    for city1, city2, d in road:
        if graph[city1-1][city2-1] == 0:
            graph[city1-1][city2-1] = d
            graph[city2-1][city1-1] = d
        elif graph[city1-1][city2-1] > d:
            graph[city1-1][city2-1] = d
            graph[city2-1][city1-1] = d

    Dijkstra(graph, dist, visited)
    for d in dist:
        if d <= K:
            answer += 1

    return answer

def Dijkstra(graph, dist, visited):
    step = 0
    while not all(visited):
        update_distance(step, graph, dist)
        step = search_next(step, dist, visited)
        if step == None:
            return
        visited[step] = True
        
def update_distance(step, graph, dist):
    for next_node, d in enumerate(graph[step]):
        if d != 0:
            if dist[step] + d < dist[next_node]:
                dist[next_node] = dist[step] + d
    
def search_next(step, dist, visited):
    next_node, min_dist = None, float('inf')
    for node, d in enumerate(dist):
        if not visited[node] and d < min_dist:
            next_node, min_dist = node, d
    return next_node