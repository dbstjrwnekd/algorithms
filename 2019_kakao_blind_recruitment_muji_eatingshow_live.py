import heapq

def solution(food_times, k):
    answer = 0
    foods = []
    prev = 0
    for i, time in enumerate(food_times):
        heapq.heappush(foods, (time, i))
    
    while foods:
        cur_time, index = heapq.heappop(foods)
        k -= (cur_time-prev) * (len(foods)+1)
        
        if k >= 0:
            prev = cur_time
        else:
            heapq.heappush(foods, (cur_time, index))
            break
    
    if not foods:
        return -1
    
    idx = k%len(foods)
    return sorted(foods, key=lambda x: x[1])[idx][1]+1
            