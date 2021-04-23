import collections

def solution(info, query):
    answer = []
    volenteers = collections.defaultdict(list)
    for data in info:
        lang, job, exp, food, score = data.split()
        possible_data = get_possible_data(lang, job, exp, food)
        set_score(volenteers, possible_data, score)

    for key in volenteers:
        volenteers[key].sort()
    
    for data in query:
        lang, job, exp, food_and_score = data.split(' and ')
        food, score = food_and_score.split()
        score = int(score)
        key = lang+job+exp+food
        answer.append(get_possible_score(volenteers, key, score))
        
    return answer

def get_possible_data(lang, job, exp, food):
    possible_list = []
    for l in [lang, '-']:
        for j in [job, '-']:
            for e in [exp, '-']:
                for f in [food, '-']:
                    possible_list.append(l+j+e+f)
    return possible_list

def set_score(volenteers, possible_data, score):
    score = int(score)
    for possible in possible_data:
        volenteers[possible].append(score)
        
def get_possible_score(volenteers, key, score):
    possible_list = volenteers[key]
    if not possible_list:
        return 0
    left, right = 0, len(possible_list)
    while left < right-1:
        mid = (left + right) // 2
        if possible_list[mid] >= score:
            right = mid
        elif possible_list[mid] < score:
            left = mid

    while left > 0 and possible_list[left] == score:
        left -= 1
        
    if left == 0 and possible_list[left] >= score:
        left -= 1
        
    return len(possible_list) - left - 1
