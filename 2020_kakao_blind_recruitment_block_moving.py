import collections

def solution(board):
    n = len(board)
    check = collections.defaultdict(int)
    answer = -1
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    queue = collections.deque([((0,0),(0,1),0,'h')])
    
    while queue:
        curNode1, curNode2, step, pos = queue.popleft()
        check[(curNode1, curNode2)] = True
        if curNode1 == (n-1,n-1) or curNode2 == (n-1, n-1):
            return step
        
        for i in range(4):
            next_x1, next_y1 = curNode1[0]+dx[i], curNode1[1]+dy[i]
            next_x2, next_y2 = curNode2[0]+dx[i], curNode2[1]+dy[i]
            if isRightPos(next_x1,n) and isRightPos(next_y1,n) and isRightPos(next_x2,n) and isRightPos(next_y2, n):
                if not check[((next_x1, next_y1),(next_x2, next_y2))] and board[next_x1][next_y1] == 0 and board[next_x2][next_y2] == 0:
                    check[((next_x1, next_y1),(next_x2, next_y2))] = True
                    queue.append(((next_x1, next_y1),(next_x2, next_y2), step+1, pos))
        
        if pos == 'h':
            next_x1, next_y1 = curNode1[0]-1, curNode1[1]
            next_x2, next_y2 = curNode2[0]-1, curNode2[1]
            if isRightPos(next_x1,n) and isRightPos(next_y1,n) and isRightPos(next_x2,n) and isRightPos(next_y2, n):
                if board[next_x1][next_y1] == 0 and board[next_x2][next_y2] == 0:
                    if not check[((next_x1, next_y1),curNode1)]:
                        queue.append(((next_x1, next_y1),curNode1,step+1, 'v'))
                        check[((next_x1, next_y1),curNode1)] = True
                    if not check[((next_x2, next_y2),curNode2)]:
                        queue.append(((next_x2, next_y2),curNode2,step+1, 'v'))
                        check[((next_x2, next_y2),curNode2)] = True
            next_x1, next_y1 = curNode1[0]+1, curNode1[1]
            next_x2, next_y2 = curNode2[0]+1, curNode2[1]
            if isRightPos(next_x1,n) and isRightPos(next_y1,n) and isRightPos(next_x2,n) and isRightPos(next_y2, n):
                if board[next_x1][next_y1] == 0 and board[next_x2][next_y2] == 0:
                    if not check[(curNode1, (next_x1, next_y1))]:
                        queue.append((curNode1,(next_x1, next_y1),step+1, 'v'))
                        check[(curNode1, (next_x1, next_y1))] = True
                    if not check[(curNode2, (next_x2, next_y2))]:
                        queue.append((curNode2, (next_x2, next_y2),step+1, 'v'))
                        check[(curNode2, (next_x2, next_y2))] = True
        else:
            next_x1, next_y1 = curNode1[0], curNode1[1]-1
            next_x2, next_y2 = curNode2[0], curNode2[1]-1
            if isRightPos(next_x1,n) and isRightPos(next_y1,n) and isRightPos(next_x2,n) and isRightPos(next_y2, n):
                if board[next_x1][next_y1] == 0 and board[next_x2][next_y2] == 0:
                    if not check[((next_x1, next_y1),curNode1)]:
                        queue.append(((next_x1, next_y1),curNode1, step+1, 'h'))
                        check[((next_x1, next_y1),curNode1)] = True
                    if not check[((next_x2, next_y2),curNode2)]:
                        queue.append(((next_x2, next_y2),curNode2, step+1, 'h'))
                        check[((next_x2, next_y2),curNode2)] = True
            next_x1, next_y1 = curNode1[0], curNode1[1]+1
            next_x2, next_y2 = curNode2[0], curNode2[1]+1
            if isRightPos(next_x1,n) and isRightPos(next_y1,n) and isRightPos(next_x2,n) and isRightPos(next_y2, n):
                if board[next_x1][next_y1] == 0 and board[next_x2][next_y2] == 0:
                    if not check[(curNode1,(next_x1,next_y1))]:
                        queue.append((curNode1,(next_x1,next_y1), step+1, 'h'))
                        check[(curNode1,(next_x1,next_y1))] = True
                    if not check[(curNode2,(next_x2,next_y2))]:
                        queue.append((curNode2,(next_x2,next_y2), step+1, 'h'))
                        check[(curNode2,(next_x2,next_y2))] = True
             
    return answer

def isRightPos(spot, n):
    return 0 <= spot < n
    