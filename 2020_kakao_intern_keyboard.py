def solution(numbers, hand):
    answer = ''
    num_spots = {0:(4,2), 1:(1,1), 2:(1,2), 3:(1,3), 4:(2,1),
               5:(2,2), 6:(2,3),7:(3,1), 8:(3,2), 9:(3,3)}
    left, right = (4,1), (4,3)
    
    for number in numbers:
        num_spot = num_spots[number]
        pushed = push(number, num_spot, left, right, hand)
        answer += pushed
        if pushed == 'L':
            left = num_spot
        else:
            right = num_spot
        
    return answer

def push(number,number_spot, left, right, hand):
    if number in [1,4,7]:
        return 'L'
    if number in [3,6,9]:
        return 'R'
    left_length = abs(left[0]-number_spot[0]) + abs(left[1] - number_spot[1])
    right_length = abs(right[0]-number_spot[0]) + abs(right[1] - number_spot[1])
    
    if left_length < right_length:
        return 'L'
    elif right_length < left_length:
        return 'R'
    
    if hand == 'left':
        return 'L'
    
    return 'R'
    