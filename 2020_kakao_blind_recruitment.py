def solution(s):
    answer = len(s)
    for i in range(1, len(s)//2+1):
        answer = min(answer, len(s) - saveCount(s, i))
    return answer

def saveCount(string, n):
    count, step, end = 0, 0, len(string)
    
    while step+n <= end:
        target = string[step:step+n]
        cur = 1
        step += n
        while string[step:step+n] == target:
            cur += 1
            step += n
        
        if cur > 1:
            count += (n*cur) - (len(str(cur)) + n)
    
    return count