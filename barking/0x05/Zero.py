import sys

result = []
n = int(sys.stdin.readline().strip())
for i in range(n):
    num = int(sys.stdin.readline().strip())
    if num == 0:
        if result:
            result.pop()
    else:
        result.append(num)

print(sum(result))