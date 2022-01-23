# 상하좌우 37:48
N = int(input())
rout = list(map(str, input().split()))

result = [1,1]
for i in rout:
    if i == 'R':
        if result[1] < 5:
            result[1] += 1
    elif i == 'U':
        if result[0] > 1:
            result[0] -= 1
    elif i == 'L':
        if result[1] > 1:
            result[0] -= 1
    elif i == 'D':
        if result[0] < 5:
            result[0] += 1

print(result[0], result[1])
