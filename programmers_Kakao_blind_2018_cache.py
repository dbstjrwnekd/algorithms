def solution(cacheSize, cities):
    answer = 0
    cash = dict()
    for city in cities:
        city = city.lower()
        answer += process_city(cash, city)
        if cacheSize > 0:
            update_cash(cash, city, cacheSize)
    
    return answer

def process_city(cash, city):
    time = 5
    if city in cash:
        time = 1
    return time
    
def update_cash(cash, city, cacheSize):
    if len(cash) == 0:
        cash[city] = 0
    else:
        for c in cash:
            cash[c] += 1
        
        cash[city] = 0
        
        if len(cash) > cacheSize:
            c = get_max_cash(cash)
            del cash[c]
        
def get_max_cash(cash):
    city = None
    max_cash = 0
    for c in cash:
        if cash[c] > max_cash:
            max_cash = cash[c]
            city = c
    return city