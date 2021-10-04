n = int(input())
fears = sorted(list(map(int, input().split())))

answer, max_fear, group = 0, 0, []
for fear in fears:
    group.append(fear)
    max_fear = max(max_fear, fear)
    if max_fear <= len(group):
        answer += 1
        group, max_fear = [], 0
        
print(answer)
