def solution(n, s, a, b, fares):
    dist = [[float('inf')] * n for _ in range(n)]
    graph = [[0] * n for _ in range(n)]
    for fare in fares:
        n1, n2, d = fare
        graph[n1-1][n2-1] = d
        graph[n2-1][n1-1] = d
    
    dijkstra_all(graph, dist, n)
    min_money = get_min_money(dist,s-1, a-1, b-1)
    
    return min_money

def get_min_money(dist, s, a, b):
    min_money = dist[s][a] + dist[s][b]
    for mid in range(len(dist)):
        if dist[s][mid] + dist[mid][a] + dist[mid][b] < min_money:
            min_money = dist[s][mid] + dist[mid][a] + dist[mid][b]
    return min_money

def dijkstra_all(graph, dist, n):
    for step, d in enumerate(dist):
        dijkstra(graph,d,step, n)

def dijkstra(graph, dist, step, n):
    check = [False] * n
    dist[step] = 0
    check[step] = 0
    while True:
        update_dist(graph, dist, step)
        step = get_next_node(dist, check)
        if step == None:
            return
        check[step] = True

def update_dist(graph, dist, step):
    for next_node, d in enumerate(graph[step]):
        if d != 0:
            if dist[step] + d < dist[next_node]:
                dist[next_node] = dist[step] + d

def get_next_node(dist, check):
    next_node = None
    min_dist = float('inf')
    for node, d in enumerate(dist):
        if not check[node]:
            if d < min_dist:
                min_dist = d
                next_node = node
    return next_node