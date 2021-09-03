def solution(price, money, count):
    answer = price * getSum(count) - money
    return answer if answer > 0 else 0

def getSum(count):
    return count*(count+1)//2
    