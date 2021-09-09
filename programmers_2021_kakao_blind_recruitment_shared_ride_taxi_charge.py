def solution(n, s, a, b, fares):
    graph = [[float('inf')] * n for i in range(n)]
    for u, v, w in fares:
        graph[u-1][v-1] = w
        graph[v-1][u-1] = w
    for i in range(n):
        graph[i][i] = 0
    
    for k in range(n):
        for f in range(n):
            for e in range(n):
                graph[f][e] = min(graph[f][e], graph[f][k]+graph[k][e])
    
    answer = graph[s-1][a-1] + graph[s-1][b-1]
    for k in range(n):
        answer = min(answer, graph[s-1][k]+graph[k][a-1]+graph[k][b-1])
    
    return answer
