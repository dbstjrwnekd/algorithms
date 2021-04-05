def solution(m, n, board):
    answer = 0
    new_board = []
    for col in range(n):
        new_row = []
        for row in range(m)[::-1]:
            new_row.append(board[row][col])
        new_board.append(new_row)
    
    while True:
        num = scan(new_board,n,m)
        if num == 0:
            break
        answer+=num
        recover(new_board,n,m)
    
    return answer

def scan(board,m,n):
    check = set()
    for i in range(m-1):
        for j in range(n-1):
            if board[i][j] != None and board[i][j] == board[i+1][j] == board[i][j+1] == board[i+1][j+1]:
                check.add((i,j))
                check.add((i,j+1))
                check.add((i+1,j))
                check.add((i+1,j+1))
    
    for x,y in check:
        board[x][y] = None
        
    return len(check)

def recover(board,m,n):
    for row in range(m):
        new_col = [None]*n
        point = 0
        for col in range(n):
            if board[row][col] != None:
                new_col[point] = board[row][col]
                point+=1
        board[row] = new_col