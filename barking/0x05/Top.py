import sys
n = int(sys.stdin.readline())
top = list(map(int, sys.stdin.readline().split()))
result = ["0"]
for i in range(1, len(top)):
    for j in range(i-1, -1, -1): # 0이 포함되도록
        if top[j] >= top[i]:
            result.append(str(j+1))
            break
    if len(result) == i:
        result.append("0")

print(" ".join(result))
# 답은 맞는데 시간 초과,, O(N^2)