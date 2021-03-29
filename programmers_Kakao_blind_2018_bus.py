import collections

def solution(n, t, m, timetable):
    answer = ''
    timetable.sort()
    timetable = collections.deque(timetable)
    ridable = {}
    start_time = '09:00'
    
    count = 0
    for i in range(n):
        ridable[start_time] = []
        while count < len(timetable) and len(ridable[start_time]) < m:
            if timetable[count] <= start_time:
                ridable[start_time].append(timetable[count])
                count+=1
            else:
                break
        start_time = add_time(start_time, t)
    time = max(ridable.keys())
    if len(ridable[time]) < m:
        answer = time
    else:
        end_time = max(ridable[time])
        answer = add_time(end_time, '-1')
    
    return answer

def add_time(start_time, time):
    hour, minute = start_time.split(':')
    minute = int(minute) + int(time)
    hour = '00' + str(int(hour) + minute // 60)
    minute = '00' + str(minute % 60)
    hour, minute = hour[-2:], minute[-2:]
    return hour + ':' + minute