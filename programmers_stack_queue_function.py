import math

def solution(progresses, speeds):
    result = []
    answer = []
    for i in range(len(progresses)):
        answer.append(math.ceil((100-progresses[i])/speeds[i]))
    while True:
        start = answer[0]
        step = 1
        while step < len(answer) and start >= answer[step]:
            step += 1
        result.append(step)
        answer = answer[step:]
        if len(answer) == 0:
            break
    
    return result