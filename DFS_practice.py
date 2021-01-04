graph = {
        1: [2,3,4],
        2: [5],
        3: [5],
        4: [],
        5: [6,7],
        6: [],
        7: [3],
}

def DFS(v, discovered=[]):
    discovered.append(v)
    for next_v in graph[v]:
        if not next_v in discovered:
            discovered = DFS(next_v,discovered)
    return discovered

print(DFS(1))

def DFS_iterative(v):
    discovered = []
    stack = [v]
    while stack:
        current = stack.pop()
        if not current in discovered:
            discovered.append(current)
            for next_v in graph[current]:
                stack.append(next_v)
    return discovered

print(DFS_iterative(1))
    