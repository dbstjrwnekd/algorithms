graph = {
        1: [2,3,4],
        2: [5],
        3: [5],
        4: [],
        5: [6,7],
        6: [],
        7: [3],
}

def BFS(v):
    discovered = []
    queue = [v]
    while queue:
        current = queue.pop(0)
        if not current in discovered:
            discovered.append(current)
            for next_v in graph[current]:
                queue.append(next_v)
    return discovered

BFS(1)