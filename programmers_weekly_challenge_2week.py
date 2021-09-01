import collections

def solution(scores):
    N = len(scores)
    answer = ''
    for j in range(N):
        scoreTable = collections.defaultdict(int)
        score = 0
        maxScore, minScore = 0, float('inf')
        for i in range(N):
            s = scores[i][j]
            score += s
            if s > maxScore: maxScore = s
            if s < minScore: minScore = s
            scoreTable[s] += 1
        s = scores[j][j]
        n = N
        if s == maxScore or s == minScore:
            if scoreTable[s] == 1:
                score -= s
                n -= 1
        if n == 0:
            answer += 'F'
            continue
        answer += getScore(score/n)
            
    return answer

def getScore(avg):
    if avg >= 90:
        return 'A'
    elif avg >= 80:
        return 'B'
    elif avg >= 70:
        return 'C'
    elif avg >= 50:
        return 'D'
    return 'F'
    