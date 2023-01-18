import math
from collections import deque
progresses = [93, 30, 55]
speeds = [1, 30, 5]
answer = []

days = deque() # 남은 작업 일수를 담는 queue
for i in range(len(progresses)):
    days.append(math.ceil((100 - progresses[i]) / speeds[i])) # 올림

cnt = 1
pop = days.popleft() # 첫번째 비교할 일수
while days:
    top = days.popleft() # 큐에 남아있는 0번째 일수
    if pop >= top:
        cnt += 1 # 같이 배포
    else:
        pop = top # 비교할 일수 갱신
        answer.append(cnt)
        cnt = 1

answer.append(cnt)
print(answer)

'''
기능개발 level 2
문제 풀이
- 각 기능별로 남은 작업 일수를 먼저 구한다.
    - '남은 일수 = (100 - 작업 진행량) / 속도'를 올림한다.
- 일수를 앞부터 비교하는데, 처음 꺼낸 비교할 일수보다 0번째 일수가 크면 같이 배포하기때문에 cnt를 올려준다.
- 비교할 일수보다 0번째 일수가 작으면 누적된 cnt를 answer에 담아주고 cnt를 초기화, 0번째를 비교할 일수로 갱신해준다.
- 큐가 하나 남았을때 popleft()로 비어지면 마지막 cnt를 넣지 못하고 while문을 탈출하기 때문에 마지막 값의 cnt를 answer에 넣어준다.
=> 문제 풀이는 맞는데.. days를 비교를 제대로 못해서 못풀었다. 왜.. 다 해놓고 답을 못 내놓니ㅜ
'''