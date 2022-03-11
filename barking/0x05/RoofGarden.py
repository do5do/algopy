from collections import deque

n = int(input())
deq = deque()
for _ in range(n):
    deq.append(input())

cnt = 0
while deq:
    topLeft = deq.popleft()
    for i in range(len(deq)):
        if topLeft > deq[i]:
            cnt += 1
        else:
            break

print(cnt)
# pypy, python 시간초과