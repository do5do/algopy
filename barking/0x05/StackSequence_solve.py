import sys

n = int(sys.stdin.readline())
result = []
stack = []
index = 1
flag = False

for _ in range(n):
    num = int(sys.stdin.readline().strip())
    while index <= num:
        stack.append(index)
        result.append("+")
        index += 1

    if stack[-1] == num:
        stack.pop()
        result.append("-")
    else:
        flag = True

if flag:
    print("NO")
else:
    print("\n".join(result))