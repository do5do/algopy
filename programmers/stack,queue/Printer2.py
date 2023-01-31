from collections import deque


def solution(priorities, location):
    # (index, priority) 객체 생성
    queue = deque([(i, priority) for i, priority in enumerate(priorities)])

    cnt = 0
    while queue:
        maxPrior = max(queue, key=lambda x: x[1]) # 최대값을 pop하기 전에 먼저 구한다.
        pop = queue.popleft()

        if pop[1] < maxPrior[1]:
            queue.append(pop)  # 뒤로 보냄
        else:
            cnt += 1  # 같으면 인쇄
            if pop[0] == location:
                return cnt

solution([2, 1, 3, 2], 2)

'''
프린터
문제 풀이
- 중요도와 인덱스를 함께 가진 객체 생성 (queue)
    - 생성한 객체의 중요도의 max값을 구해서 그 값보다 작으면 뒤로 보낸다.
    - max값과 같으면 (큰 값은 없음) 인쇄. 
        - location을 확인해서 출력 번호를 리턴한다.
=> 34분 소요. 최대값을 pop하고 나서 구해서 런타임 에러가 몇개 있었다. -> 로직 내에서 최대값과 같은 값을 찾지 못해서 시간초과 난듯
'''