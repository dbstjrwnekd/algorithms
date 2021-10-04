spot = input()
row, col = ord(spot[0]) - ord('a'), int(spot[1])-1

dx = [2,2,-2,-2,1,1,-1,-1]
dy = [1,-1,1,-1,2,-2,2,-2]
answer = 0
for i in range(8):
    next_x, next_y = row+dx[i], col+dy[i]
    if 0 <= next_x < 8 and 0 <= next_y < 8:
        answer += 1
print(answer)
