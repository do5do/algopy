from collections import deque


def solution(n, lost, reserve):
    answer = 0
    lost.sort()
    reserve.sort()
    lost = deque(lost)

    for i in range(1, n + 1): # 수업 가능
        if i in lost and i in reserve: # reserve에서 도난 당한 사람 제거
            lost.remove(i)
            reserve.remove(i)

        if i not in lost:
            answer += 1

    for re in reserve: # lost 구제 확인
        if lost:
            if re + 1 in lost or re - 1 in lost:
                answer += 1
                lost.popleft()
    return answer


print(solution(4, [2, 3],[3, 4]))

'''
- 수업을 무조건 들을 수 있는 사람을 먼저 구한다. -> lost가 아닌 사람
- reserve에 있는 사람이 lost중 누군가를 구제할 수 있는지 확인 한다.
    - lost중 한명을 구제했다면 다음 사람이 구제된 사람을 또 구제할 필요가 없으니 lost에서 제거해준다.
=> 1차 시도
- 60점임.. 테케 몇개 실패. reserve에서 도난당한 사람이 있을 수도 있다는 조건을 무시해서 그런듯
- reserve에서 도난 당한 사람을 reserve에서도 무시하고 lost에서도 제거해줘야 한다.
'''