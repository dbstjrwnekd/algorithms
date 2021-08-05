import collections

def solution(priorities, location):
    answer = 0
    priorities = collections.deque(priorities)
    while len(priorities) > 1:
        #맨 앞을 뺀다
        target = priorities.popleft()
        location -= 1
        
        #뺀 값이 최대값인 경우
        if target >= max(priorities):
            answer += 1
            if location == -1:
                return answer
        else:#최대값이 아닌 경우
            priorities.append(target)
            if location < 0:
                location = len(priorities) - 1
        
    return answer+1