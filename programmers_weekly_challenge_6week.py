def solution(weights, head2head):
    answer = []
    winScore = {}
    for i, w in enumerate(weights):
        winScore[i+1] = {
            'number': i + 1,
            'weight': w,
            'higher': 0,
            'lighter': 0,
            'fight': 0
        }
    
    for i in range(len(head2head)):
        for j in range(len(head2head[i])):
            if head2head[i][j] != 'N':
                winScore[i+1]['fight'] += 1
            if head2head[i][j] == 'W':
                if weights[i] < weights[j]:
                    winScore[i+1]['higher'] += 1
                else:
                    winScore[i+1]['lighter'] += 1
    
    answer = winScore.keys()
    answer = sorted(answer, key=lambda x: (-(winScore[x]['higher']+winScore[x]['lighter'])/winScore[x]['fight'] if winScore[x]['fight'] != 0 else 0, -winScore[x]['higher'], -weights[x-1], winScore[x]['number']))
    
    for i, w in enumerate(answer):
        answer[i] = winScore[w]['number']
    
    return answer
    