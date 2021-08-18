def solution(cacheSize, cities):
    answer = 0
    cache = {}
    for city in cities:
        city = city.lower()
        if cacheSize == 0:
            answer+=5
            continue
           
        for c in cache: cache[c] += 1
            
        if city in cache:
            cache[city] = 0
            answer += 1
        else:
            answer += 5
            if len(cache) < cacheSize:
                cache[city] = 0
            else:
                lru = sorted(cache.keys(), key=lambda x: -cache[x])[0]
                del cache[lru]
                cache[city] = 0
    
    return answer
