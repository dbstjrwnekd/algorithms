s = input()
answer = 0

for n in s:
    num = int(n)
    answer = max(answer+num, answer*num)

print(answer)
