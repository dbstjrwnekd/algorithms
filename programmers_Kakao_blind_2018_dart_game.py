def solution(dartResult):
    answer = 0
    scores = create_score(dartResult)
    return sum(scores)

def create_score(dartResult):
    scores = []
    top = -1
    pointer = 0
    while pointer < len(dartResult):
        mark = dartResult[pointer]
        if mark.isnumeric():
            step = pointer+1
            while dartResult[step].isnumeric():
                mark += dartResult[step]
                step += 1
            scores.append(int(mark))
            top += 1
            pointer = step
            continue
        elif mark in 'SDT':
            if mark == 'D':
                scores[top] **= 2
            elif mark == 'T':
                scores[top] **= 3
        elif mark in '*#':
            if mark == '*':
                scores[top] *= 2
                if top > 0:
                    scores[top-1] *= 2
            elif mark == '#':
                scores[top] *= -1
        pointer += 1
    return scores