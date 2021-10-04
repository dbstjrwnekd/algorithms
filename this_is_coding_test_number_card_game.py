n, m = list(map(int, input().split()))
board = []
for i in range(n):
    board.append(list(map(int,input().split())))

maximum = 0

for row in range(len(board)):
    min_value = min(board[row])
    maximum = max(maximum, min_value)
print(maximum)
