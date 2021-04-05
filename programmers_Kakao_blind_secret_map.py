def solution(n, arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        b1 = num_to_bin(arr1[i],n)
        b2 = num_to_bin(arr2[i],n)
        row = ''
        for j in range(len(b1)):
            if b1[j] == '0' and b2[j] == '0':
                row+=' '
            else:
                row+='#'
        answer.append(row)
        
    return answer

def num_to_bin(num,n):
    return format(num, 'b').zfill(n)