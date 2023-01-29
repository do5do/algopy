# 다시 풀기 : 2회차
from collections import deque
import math


def solution(progresses, speeds):
    answer = []
    days = deque()

    # 남은 일수를 구한다.
    for i in range(len(progresses)):
        days.append(math.ceil((100 - progresses[i]) / speeds[i]))

    pop = days.popleft()  # 처음 비교할 일수
    cnt = 1
    while days:
        top = days.popleft()
        if pop >= top:
            cnt += 1
        else:
            answer.append(cnt)
            cnt = 1  # cnt 초기화
            pop = top  # 비교할 수 교체

    answer.append(cnt)
    return answer

solution([93, 30, 55], [1, 30, 5])

'''
기능개발
문제 풀이
- 남은 일수를 구한다.
- 남은 일수의 값을 비교한다.
    - 첫번째 비교할 수가 두번째 수보다 크면 카운트를 더해준다. -> 크거나 같을때로 해야하는데, 같을때를 안해줘서 테케 4개 틀림
    - 작으면 answer에 카운트를 넣고, 카운트를 초기화 한다.
        - 비교 하는 수를 교체 한다.
- 마지막 카운트를 answer에 넣어준다.
=> 풀이는 전과 완전 똑같고 20분 이상 걸림..
'''