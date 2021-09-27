def solution(key, lock):
    answer = False
    for i in range(4):
        N, M = 2*(len(key)-1)+len(lock), 2*(len(key[0])-1)+len(lock[0])
        box = boxInsert(N, M, key, lock)
        if check(key, box):
            answer = True
            break
        key = rotate(key)
    
    return answer

def rotate(arr):
    newArr = []
    for j in range(len(arr[0])):
        row = []
        for i in range(len(arr)-1,-1,-1):
            row.append(arr[i][j])
        newArr.append(row)
    return newArr

def check(key, box):
    for x in range(len(box)-(len(key)-1)):
        for y in range(len(box[0])-(len(key[0])-1)):
            keyInsert(x, y, key, box)
            if isOpen(key, box):
                return True
            keyRemove(x, y, key, box)
    return False
    
def keyInsert(x, y, key, box):
    for i in range(len(key)):
        for j in range(len(key[0])):
            box[x+i][y+j] += key[i][j]

def keyRemove(x, y, key, box):
    for i in range(len(key)):
        for j in range(len(key[0])):
            box[x+i][y+j] -= key[i][j]

def isOpen(key, box):
    start_x, start_y = len(key)-1, len(key[0])-1
    for x in range(start_x, len(box)-(len(key)-1)):
        for y in range(start_y, len(box[0])-(len(key[0])-1)):
            if box[x][y] != 1:
                return False
    return True
    
def boxInsert(N, M, key, lock):
    box = [[0] * M for i in range(N)]
    start_x, start_y = len(key)-1, len(key[0])-1
    box_x = start_x
    for x in range(len(lock)):
        box_y = start_y
        for y in range(len(lock[0])):
            box[box_x][box_y] = lock[x][y]
            box_y += 1
        box_x += 1
    return box
    