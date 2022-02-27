from collections import deque

n, k = map(int, input().split())
li = (i for i in range(1, n+1))
deq = deque(li)
result = []

while deq:
    for i in range(k):
        if i == k-1:
            result.append(deq.popleft())
        else:
            deq.append(deq.popleft())

# 출력
print("<", end="")
for i in range(len(result)):
    if i == len(result) - 1:
        print(result[i], end="")
    else:
        print(result[i], end=", ")
print(">", end="")

# 출력 간단하게 -> result에 원소를 담을때 string으로 담아야 join할 수 있음
# print(f'<{", ".join(result)}>')

