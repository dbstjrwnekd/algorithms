class Node:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right

def solution(n, k, cmd):
    answer = ''
    head = tail = cur = Node("head", None, None)
    for i in range(n):
        node = Node(i, tail, None)
        tail.right = node
        tail = tail.right
        if i <= k:
            cur = cur.right
    deletedQueue = []
    deletedKey = {}
    
    for c in cmd:
        c = c.split()
        action = c[0]
        if action == 'U':
            length = int(c[1])
            for i in range(length):
                cur = cur.left
        elif action == 'D':
            length = int(c[1])
            for i in range(length):
                cur = cur.right
        elif action == 'C':
            deleted = cur
            if cur.right:
                cur = cur.right
            else:
                cur = cur.left
            if deleted.left:
                deleted.left.right = deleted.right
            if deleted.right:
                deleted.right.left = deleted.left
            deletedQueue.append(deleted)
            deletedKey[deleted.data] = 1
        else:
            recover = deletedQueue.pop()
            recoverLeft, recoverRight = recover.left, recover.right
            while recoverLeft and recoverLeft.data in deletedKey:
                recoverLeft = recoverLeft.left
            while recoverRight and recoverRight.data in deletedKey:
                recoverRight = recoverRight.right
            recover.left = recoverLeft
            recover.right = recoverRight
            if recoverLeft:
                recoverLeft.right = recover
            if recoverRight:
                recoverRight.left = recover
            
            del deletedKey[recover.data]
    for i in range(n):
        if i in deletedKey:
            answer += 'X'
        else:
            answer += 'O'
    
    return answer