s = input()
nums = {'0':0, '1':0}

step = 0
current = s[step]

while step < len(s):
    if current != s[step]:
        nums[s[step]]+=1
        current = s[step]
    step+=1
print(max(nums.values()))
