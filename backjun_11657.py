import collections

n, m = map(int, input().split())
dist = [float('inf')] * n
graph = collections.defaultdict(list)
edges = 0


for i in range(m):
    c1, c2, d = map(int, input().split())
    graph[c1-1].append((c2-1, d))
    edges+=1

dist[0] = 0

for i in range(edges-1):
    for c in range(len(dist)):
        if dist[c] != float('inf') and c in graph:
            for c2, d in graph[c]:
                if dist[c] + d < dist[c2]:
                    dist[c2] = dist[c]+d
flag = True
for c in range(len(dist)):
    isbreak = False
    if dist[c] != float('inf') and c in graph:
        for c2, d in graph[c]:
            if dist[c] + d < dist[c2]:
                flag = False
                isbreak = True
                break
    if isbreak:
        break
    
if not flag:
    print(-1)
else:
    for e in dist[1:]:
        if e != float('inf'):
            print(e)
        else:
            print(-1)