from itertools import permutations
import heapq


def solution(jobs):
    answer = []
    heapq.heapify(answer)
    permute = list(permutations(jobs, len(jobs)))

    for jobs in permute:
        totalTime = 0
        sumJobs = 0

        for job in jobs:
            sumJobs += job[1]
            totalTime += sumJobs - job[0]

        heapq.heappush(answer, totalTime // len(jobs))
    return answer[0]

print(solution([[0, 3], [1, 9], [2, 6]]))


'''
디스크 컨트롤러 level 3
문제 풀이
- job의 순열대로 평균을 모두 구하여 비교한다?
    - abc, acb, bac, bca, cab, cba (permutation)
    - 순열을 구한 다음 하나씩 처리 시간의 평균을 구한다.
        - (소요 시간 - 요청 시점)인데 소요 시간은 누적하여 더해주고 해당 번째의 소요 시간을 뺀다.
    - 평균을 힙에 넣고 힙 정렬 후 0번째 출력
=> 모든 조합을 구하고 힙 정렬을 하면 답은 맞지만 테케 하나 빼고 모두 시간 초과다. 예상했지...
'''