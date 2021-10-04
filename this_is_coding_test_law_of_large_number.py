n, m, k = list(map(int, input().split()))
nums = list(map(int,input().split()))

nums.sort(reverse=True)
answer = 0
count = 0
cur_index = 0
for i in range(m):
    if count < k:
        answer += nums[cur_index]
        count+=1
    else:
        if cur_index != 0:
            cur_index = 0
        else:
            cur_index += 1
        count = 0
print(answer)
