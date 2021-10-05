import collections

n, m = map(int, input().split())

nums = list(map(int,input().split()))
answer = 0

table = collections.defaultdict(int)
total = n

for n in nums:
    table[n] += 1

for n in table.keys():
    answer += table[n]*(total-table[n])
    total -= table[n]
print(answer)
