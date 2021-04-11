def solution(prices):
    answer = []
    for i in range(len(prices)):
        flag = True
        time = 0
        for j in range(i+1, len(prices)):
            time+=1
            if prices[j] < prices[i]:
                answer.append(time)
                flag = False
                break
        if flag:
            answer.append(time)
    return answer