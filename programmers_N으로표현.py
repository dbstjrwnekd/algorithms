import collections

def solution(N, number):
    n_table = collections.defaultdict(set)
    
    if number == N:
        return 1
    
    for i in range(1,8+1):
        n_table[i].add(int(str(N)*i))
    
    
    for i in range(2,8+1):
        for j in range(1,i):
            for num1 in n_table[j]:
                for num2 in n_table[i-j]:
                    n_table[i].add(num1+num2)
                    n_table[i].add(num1-num2)
                    n_table[i].add(num1*num2)
                    if num2 != 0:
                        n_table[i].add(num1//num2)
        if number in n_table[i]:
            return i
    return -1
