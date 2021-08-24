def solution(places):
    answer = []
    for place in places:
        answer.append(isSafeRoom(place))
    return answer

def isSafeRoom(roomData):
    DEFAULT_LENGTH = 5
    
    board = []
    for data in roomData:
        board.append(list(data))
    
    dx, dy = [0,0,1,-1], [1,-1,0,0]
    d2x, d2y = [0,0,2,-2], [2,-2,0,0]
    ddigx, ddigy = [-1,-1,1,1], [1,-1,1,-1]
    DELTA = 4
    
    for x in range(DEFAULT_LENGTH):
        for y in range(DEFAULT_LENGTH):
            if board[x][y] == 'P':
                for i in range(DELTA):
                    """
                    up/down/left/right test
                    if P exist return 0
                    """
                    next_x, next_y = x+dx[i], y+dy[i]
                    if 0 <= next_x < DEFAULT_LENGTH and 0 <= next_y < DEFAULT_LENGTH:
                        if board[next_x][next_y] == 'P':
                            return 0
                    """
                    up/down/left/right 2 length test
                    if P exist and not exist partition, return 0
                    """
                    next_x, next_y = x+d2x[i], y+d2y[i]
                    if 0 <= next_x < DEFAULT_LENGTH and 0 <= next_y < DEFAULT_LENGTH:
                        if board[next_x][next_y] == 'P':
                            mid_x, mid_y = (next_x+x)//2, (next_y+y)//2
                            if board[mid_x][mid_y] != 'X':
                                return 0
                    """
                    diagonal test
                    if P exist and not exist partition in each side, return 0
                    """
                    next_x, next_y = x+ddigx[i], y+ddigy[i]
                    if 0 <= next_x < DEFAULT_LENGTH and 0 <= next_y < DEFAULT_LENGTH:
                        if board[next_x][next_y] == 'P':
                            if board[x][next_y] != 'X' or board[next_x][y] != 'X':
                                return 0
                board[x][y] = 'O'
    return 1