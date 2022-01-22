odd = []
nums = []
for _ in range(7):
    nums.append(int(input()))

for i in nums:
    if i % 2 == 1:
        odd.append(i)

if len(odd): # 홀수가 없을때
    print(sum(odd))
    print(min(odd))
else:
    print(-1)