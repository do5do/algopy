import sys

s = list(sys.stdin.readline().strip())
n = int(input())

rightStack = []
for _ in range(n):
    command = sys.stdin.readline()
    if command[0] == 'L':
        if len(s) == 0:
            continue
        rightStack.append(s.pop())
    elif command[0] == 'D':
        if len(rightStack) == 0:
            continue
        s.append(rightStack.pop())
    elif command[0] == 'B':
        if len(s) == 0:
            continue
        s.pop()
    else:
        s.append(command[2])

s.extend(reversed(rightStack))
print(''.join(s))