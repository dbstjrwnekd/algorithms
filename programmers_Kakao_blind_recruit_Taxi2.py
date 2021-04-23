import collections

def solution(n, s, a, b, fares):
    graph = collections.defaultdict(list)
    dist = [[float('inf')] * n for _ in range(n)]
    
    for u, v, w in fares:
        graph[u-1].append((v-1,w))
        graph[v-1].append((u-1,w))
        dist[u-1][v-1] = dist[v-1][u-1] = w

    for i in range(n):
        dist[i][i] = 0
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    answer = dist[s-1][a-1] + dist[s-1][b-1]
    for k in range(n):
        answer = min(answer, dist[s-1][k] + dist[k][a-1] + dist[k][b-1])
    
    return answer
