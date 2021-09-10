def solution(play_time, adv_time, logs):
    answer = ''
    play_time = time_to_num(play_time)
    adv_time = time_to_num(adv_time)
    timeTable = [0] * (play_time+1)
    
    for log in logs:
        start_time, end_time = log.split('-')
        start_time = time_to_num(start_time)
        end_time = time_to_num(end_time)
        timeTable[start_time] += 1
        timeTable[end_time] -= 1
        
    for i in range(1, len(timeTable)):
        timeTable[i] = timeTable[i]+timeTable[i-1]
    
    for i in range(1, len(timeTable)):
        timeTable[i] = timeTable[i]+timeTable[i-1]
        
    maxTime = timeTable[adv_time-1]
    answer = 0
    
    for i in range(adv_time-1, play_time):
        time = timeTable[i]-timeTable[i-adv_time]
        if time > maxTime:
            maxTime = time
            answer = i-adv_time+1
    
    
    return num_to_time(answer)

def time_to_num(time):
    h, m, s = time.split(':')
    return int(h)*3600 + int(m)*60 + int(s)
    
    
def num_to_time(num):
    h = num // 3600
    num %= 3600
    m = num // 60
    num %= 60
    s = num
    
    h = str(h) if h > 9 else '0'+str(h)
    m = str(m) if m > 9 else '0'+str(m)
    s = str(s) if s > 9 else '0'+str(s)
    return h+':'+m+':'+s
    