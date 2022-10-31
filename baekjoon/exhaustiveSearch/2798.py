from itertools import *

n, m = map(int, input().split())
nums = list(permutations(map(int, input().split()), 3))
least = 0

for num in nums:
    sums = sum(num)
    if sums == m:
        least = sums
        break
    elif sums < m:
        if least < sums:
            least = sums
    else:
        continue

print(least)

'''
level: 브론즈 2
오늘의 교훈: permutations를 쓰지 말고 구현해보자!
순열 라이브러리 하나 알았다고 너무 의존하는 것 같다.
제일 먼저 모든 조합을 구하기 위해 permutations 부터 사용하려고 했다..
'''