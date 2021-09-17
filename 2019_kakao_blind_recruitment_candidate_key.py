import collections

def solution(relation):
    columns = [i for i in range(len(relation[0]))]
    comb = getComb(columns)
    return getKeys(comb, relation)

def getComb(columns):
    combs = []
    def comb(index, found):
        if found:
            combs.append(found[:])
        
        for i in range(index+1, len(columns)):
            comb(i, found+(i,))
    comb(-1, ())
    return collections.deque(sorted(combs, key= lambda x: len(x)))
        
def getKeys(comb, relation):
    candiKeys = {}
    while comb:
        keys = comb.popleft()

        if keys == None:
            continue
        
        isCandi = True
        records = {}
        for record in relation:
            recordInfo = ''
            for key in keys:
                recordInfo += str(record[key])
            if not recordInfo in records:
                records[recordInfo] = 1
            else:
                isCandi = False
                break
        if isCandi:
            candiKeys[keys] = True
            for i, keySet in enumerate(comb):
                if not keySet:
                    continue
                keyCount = 0
                for k in keys:
                    if k in keySet:
                        keyCount += 1
                if keyCount == len(keys):
                    comb[i] = None
                        
    return len(candiKeys)
    