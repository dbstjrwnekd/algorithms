import collections
DEFAULT_LENGTH = 4

def solution(board, r, c):
    answer = [float('inf')]
    cardPos = getInitPos(board)
    permutation = []
    getPermutation(list(cardPos.keys()),[False]*len(cardPos),[],permutation)
    def getMinCount(permu, sx, sy, index, count):
        if index == len(permu):
            answer[0] = min(answer[0], count)
            return
        
        card = permu[index]
        nx, ny, newCount = bfs(sx, sy, cardPos[card][0][0], cardPos[card][0][1], count, board)
        n2x, n2y, newCount = bfs(nx, ny, cardPos[card][1][0], cardPos[card][1][1], newCount, board)
        remove(board, cardPos, card)
        getMinCount(permu, n2x, n2y, index+1, newCount)
        restore(board, cardPos, card)
        
        nx, ny, newCount = bfs(sx, sy, cardPos[card][1][0], cardPos[card][1][1], count, board)
        n2x, n2y, newCount = bfs(nx, ny, cardPos[card][0][0], cardPos[card][0][1], newCount, board)
        remove(board, cardPos, card)
        getMinCount(permu, n2x, n2y, index+1, newCount)
        restore(board, cardPos, card)
    
    for permu in permutation:
        getMinCount(permu, r, c, 0, 0)
    
    return answer[0]

#카드 위치 정보 저장
def getInitPos(board):
    cardPos = collections.defaultdict(list)
    for x in range(DEFAULT_LENGTH):
        for y in range(DEFAULT_LENGTH):
            if board[x][y] != 0:
                cardPos[board[x][y]].append((x,y))
    return cardPos

#카드 뒤집기 (0으로 만들기)
def remove(board, cardPos, card):
    for x, y in cardPos[card]:
        board[x][y] = 0
#카드 되살리기     
def restore(board, cardPos, card):
    for x, y in cardPos[card]:
        board[x][y] = card

def bfs(sx, sy, ex, ey, count, board):
    visited = [[False] * DEFAULT_LENGTH for i in range(DEFAULT_LENGTH)]
    visited[sx][sy] = True
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    queue = collections.deque([(sx, sy, count)])
    while queue:
        cur_x, cur_y, count = queue.popleft()
        if cur_x == ex and cur_y == ey:
            return (cur_x, cur_y, count + 1)
        for i in range(4):
            #상하좌우 방향기
            nx, ny = cur_x + dx[i], cur_y + dy[i]
            if isRightDot(nx, ny):
                if not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx, ny, count+1))
            #ctrl + 방향키
            nx, ny = ctrlMove(cur_x, cur_y, dx[i], dy[i], board)
            if isRightDot(nx, ny):
                if not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx, ny, count+1))
            
    
def ctrlMove(sx, sy, dx, dy, board):
    nx, ny = sx, sy
    while True:
        nx, ny = nx+dx, ny+dy
        if isRightDot(nx, ny):
            if board[nx][ny] != 0:
                return [nx, ny]
        else:
            return [nx-dx, ny-dy]
        
def isRightDot(x,y):
    if 0 <= x < DEFAULT_LENGTH and 0 <= y < DEFAULT_LENGTH:
        return True
    return False
    
def getPermutation(keys, visited, found, result):
    if len(found) == len(keys):
        result.append(found[:])
        return
    
    for i in range(len(keys)):
        if not visited[i]:
            visited[i] = True
            getPermutation(keys, visited, found+[keys[i]], result)
            visited[i] = False
            