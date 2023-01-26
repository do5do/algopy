# 두번째 solve
from collections import deque


def solution(arr):
    answer = []
    queue = deque(arr)  # queue 생성

    while queue:  # queue가 빌때까지 반복
        pop = queue.popleft()

        # answer의 마지막 원소와 첫번째 원소가 다를때만 담기
        if answer:
            if pop != answer[len(answer) - 1]:
                answer.append(pop)
        else:
            answer.append(pop)
    return answer


'''
같은 숫자는 싫어 문제 풀이
- answer에 값을 하나씩 보고 비교해서 담는다.
    - 배열에서 첫번째 원소를 빼서 answer에 넣는다. 
    - 다음 원소를 뽑아서 answer의 가장 뒷 원소와 같은 수가 아니면 answer에 넣는다.
    - arr이 빌때까지 반복한다.
=> 14분 걸림
'''
