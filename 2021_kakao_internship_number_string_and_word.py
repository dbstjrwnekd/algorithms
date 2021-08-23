def solution(s):
    numberTable = {
        'zero':'0', 
        'one':'1',
        'two':'2',
        'three':'3',
        'four':'4',
        'five':'5',
        'six':'6',
        'seven':'7',
        'eight':'8',
        'nine':'9'
    }
    
    answer = ''
    step = 0
    current = ''
    while step < len(s):
        if s[step].isnumeric():
            answer += s[step]
            step += 1
        else:
            while step < len(s) and not s[step].isnumeric():
                current += s[step]
                step += 1
                if current in numberTable:
                    break
                
            answer += numberTable[current]
            current = ''
    
    return int(answer)
