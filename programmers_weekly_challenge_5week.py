def solution(word):
    answer = 0
    alphaNum = {'cur': 0}
    alphaSet = ['A','E','I','O','U']
    def dfs(found):
        if len(found) > 5:
            return
        
        if found not in alphaNum:
            alphaNum[found] = alphaNum['cur']
            alphaNum['cur'] += 1
        
        for s in alphaSet:
            dfs(found+s)
    dfs('')
    answer = alphaNum[word]
    return answer
    