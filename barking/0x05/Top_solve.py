import sys

n = int(sys.stdin.readline())
top = list(map(int, sys.stdin.readline().split()))
result = []
stack = []

for i in range(len(top)):
    while stack:
        if top[i] > stack[-1][1]:
            stack.pop()
        else:
            result.append(stack[-1][0] + 1)
            break
    if not stack:
        result.append(0)
    stack.append((i, top[i])) # index와 함께 저장

print(" ".join(map(str, result)))
