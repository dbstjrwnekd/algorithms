DEFAULT_LANGUAGES = ['cpp', 'java', 'python']
DEFAULT_JOBS = ['backend', 'frontend']
DEFAULT_CARRIERS = ['junior', 'senior']
DEFAULT_FOODS = ['chicken', 'pizza']

def solution(info, query):
    answer = []
    candiTable = getCandiTable()
    for data in info:
        lang, job, carrier, food, score = data.split()
        candiTable[lang][job][carrier][food].append(int(score))
        
    for lang in DEFAULT_LANGUAGES:
        for job in DEFAULT_JOBS:
            for carrier in DEFAULT_CARRIERS:
                for food in DEFAULT_FOODS:
                    candiTable[lang][job][carrier][food].sort()
            
        
    for q in query:
        lang, job, carrier, foodAndScore = q.split(' and ')
        food, score = foodAndScore.split()
        answer.append(getCandiCount(candiTable, lang, job, carrier, food, int(score)))
        
    return answer

def getCandiTable():
    candiTable = {}
    for lang in DEFAULT_LANGUAGES:
        candiTable[lang] = {}
        for job in DEFAULT_JOBS:
            candiTable[lang][job] = {}
            for carrier in DEFAULT_CARRIERS:
                candiTable[lang][job][carrier] = {}
                for food in DEFAULT_FOODS:
                    candiTable[lang][job][carrier][food] = []
    return candiTable
    
def getCandiCount(candiTable, lang, job, carrier, food, score):
    langs, jobs, carriers, foods = [], [], [], []
    if lang == '-':
        langs = DEFAULT_LANGUAGES
    else:
        langs = [lang]
    if job == '-':
        jobs = DEFAULT_JOBS
    else:
        jobs = [job]
    if carrier == '-':
        carriers = DEFAULT_CARRIERS
    else:
        carriers = [carrier]
    if food == '-':
        foods = DEFAULT_FOODS
    else:
        foods = [food]
        
    count = 0
    for lang in langs:
        for job in jobs:
            for carrier in carriers:
                for food in foods:
                    candiScores = candiTable[lang][job][carrier][food]
                    left, mid, right = 0, 0, len(candiScores)
                    while left+1 < right:
                        mid = (left+right)//2
                        if candiScores[mid] < score:
                            left = mid
                        elif candiScores[mid] > score:
                            right = mid
                        else:
                            break
                    while mid > 0 and candiScores[mid] >= score:
                        mid -= 1
                    if candiScores:
                        if candiScores[mid] >= score:
                            count += len(candiScores) - mid
                        else:
                            count += len(candiScores) - mid - 1
                       
    return count
    