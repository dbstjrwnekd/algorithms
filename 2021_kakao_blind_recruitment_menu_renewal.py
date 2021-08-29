import collections

def solution(orders, course):
    answer = []
    for c in course:
        menuList = []
        for order in orders:
            menuList += getMenuList(order, c)
        topTwoMenu = collections.Counter(menuList).most_common()
        
        if not topTwoMenu: continue
        menu, N = topTwoMenu[0]
        if N > 1:
            for i in range(len(topTwoMenu)):
                menu, n = topTwoMenu[i]
                if n != N: break
                answer.append(menu)
    
    return sorted(answer)

def getMenuList(order, c):
    menuList = []
    
    def dfs(found, cur, limit):
        if len(found) == limit:
            menuList.append(''.join(sorted(list(found))))
            return
        
        for i in range(cur+1, len(order)):
            dfs(found+order[i], i, limit)
    for i in range(len(order)):
        dfs(order[i], i, c)

    return menuList
    