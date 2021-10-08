def solution(n, s, a, b, fares):
    graph = [[float('inf')] * n for i in range(n)]
    for start, end, w in fares:
        graph[start-1][end-1] = w
        graph[end-1][start-1] = w
        
    for i in range(n):
        graph[i][i] = 0
    
    for mid in range(n):
        for start in range(n):
            for end in range(n):
                graph[start][end] = min(graph[start][end], graph[start][mid] + graph[mid][end])
    
    answer = graph[s-1][a-1] + graph[s-1][b-1]
    for mid in range(n):
        answer = min(answer, graph[s-1][mid] + graph[mid][a-1] + graph[mid][b-1])
    
    return answer
    