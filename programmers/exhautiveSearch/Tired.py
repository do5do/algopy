from itertools import permutations
import time


def solution(k, dungeons):
    answer = -1
    permut = permutations(dungeons, len(dungeons))

    for dungeon in permut:
        cnt = 0
        tmpK = k
        for default, used in dungeon:
            if tmpK >= default:
                tmpK -= used # 탐험
                cnt += 1

        if cnt == len(dungeons):
            return cnt

        answer = max(answer, cnt)
    return answer

start = time.perf_counter()
print(solution(80, [[80,20],[50,40],[30,10]]))
end = time.perf_counter()
print(end - start)


'''
피로도 level 2
- 가장 쉬운 방법은 모든 경우를 차레대로 살펴보고 탐험 횟수를 카운트 하여 가장 큰 수를 리턴하는 것
    -  이 방법밖에 생각안나서 일단 해봤는데 바로 되네?
=> 30분 소요
'''