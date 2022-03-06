import sys

stack = []
def push(item):
    stack.append(item)

def top():
    if stack:
        print(stack[-1]) # 가장 위 정수 출력
    else:
        print(-1)

def size():
    print(len(stack))

def empty():
    if stack:
        print(0)
    else:
        print(1)

def pop():
    if stack:
        print(stack.pop())
    else:
        print(-1)

n = int(sys.stdin.readline().rstrip())
for i in range(n):
    cmd = sys.stdin.readline().rstrip()
    if cmd.startswith("push"):
        push(cmd.split()[1])
    elif cmd == "top":
        top()
    elif cmd == "size":
        size()
    elif cmd == "empty":
        empty()
    else:
        pop()