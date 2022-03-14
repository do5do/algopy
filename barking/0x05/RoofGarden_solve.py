import sys

n = int(sys.stdin.readline())
building = []
cnt = 0
stack = []
for _ in range(n):
    building.append(int(sys.stdin.readline().strip()))

for b in building:
    while stack and stack[-1] <= b:
        stack.pop()
    cnt += len(stack)
    stack.append(b)

print(cnt)
# point : 현재 빌딩을 이전 빌딩이 바라 볼 수 있는지를 센다.