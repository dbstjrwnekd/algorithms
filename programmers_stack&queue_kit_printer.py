import collections

def solution(priorities, location):
    answer = 0
    priorities = collections.deque(priorities)
    while True:
        front = priorities.popleft()
        
        if not priorities:
            answer += 1
            break
            
        if front >= max(priorities):
            answer += 1
            if location == 0:
                break
            location -= 1
        else:
            priorities.append(front)
            if location == 0:
                location = len(priorities) - 1
            else:
                location -= 1
    return answer