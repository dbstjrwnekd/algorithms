import copy

def solution(triangle):
    answer = copy.deepcopy(triangle)
    
    for i in range(len(triangle)-1):
        for j in range(len(triangle[i])):
            answer[i+1][j] = max(answer[i+1][j], triangle[i+1][j]+answer[i][j])
            answer[i+1][j+1] = max(answer[i+1][j+1], triangle[i+1][j+1]+answer[i][j])
            
    return max(answer[len(answer)-1])