import math
from collections import deque
progresses = [93, 30, 55]
speeds = [1, 30, 5]
answer = []

days = deque() # 남은 작업 일수를 담는 queue
for i in range(len(progresses)):
    days.append(math.ceil((100 - progresses[i]) / speeds[i])) # 올림

cnt = 1
pop = days.popleft()
while days:
    if len(days) == 1:
        if pop > days[0]:
            cnt += 1
        else:
            answer.append(cnt)
            cnt = 1
        answer.append(cnt)
        break

    if pop > days[0]: # 첫번째 원소가 뒤에 원소보다 작으면
        cnt += 1
        days.popleft() # 작은 수는 버림
    else:
        answer.append(cnt)
        cnt = 1
        pop = days.popleft() # pop 갱신

print(answer)

'''
기능개발 level 2
문제 풀이


=> 문제 풀이는 맞는거 같은데.. days를 비교 못해서 못풀었다. 하ㅠㅠ
'''