# 다시 풀기 : 2회차
from collections import deque


def solution(s):
    answer = []
    queue = deque(s)

    while queue:
        pop = queue.popleft()
        if pop == '(':
            answer.append(pop)
        else:
            if answer:
                answer.pop()  # 맨 뒤 요소 꺼내기
            else:  # 첫번째 요소가 닫힌 괄호일 때
                return False

    if answer:
        return False
    else:
        return True

'''
올바른 괄호
문제 풀이
- 괄호의 짝이 맞는지 확인한다.
    - 첫번째를 뽑았을 때 열린 괄호이면 stack에 담는다.
    - 닫힌 괄호이면 stack에 있는 열린괄호 하나를 제거한다.
    - stack이 비어있으면 True, 비어있지 않으면 False를 반환한다.
'''