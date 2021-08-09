def solution(record):
    answer = []
    userInfo = {}
    entered = []
    for r in record:
        action, *other = r.split(' ')
        if action == 'Enter':
            user_id, nick = other
            userInfo[user_id] = nick
            answer.append("님이 들어왔습니다.")
            entered.append(user_id)
        elif action == 'Change':
            user_id, nick = other
            userInfo[user_id] = nick
        else:
            user_id = other[0]
            answer.append("님이 나갔습니다.")
            entered.append(user_id)
    
    for i in range(len(answer)):
        answer[i] = userInfo[entered[i]] + answer[i]
    
    return answer
