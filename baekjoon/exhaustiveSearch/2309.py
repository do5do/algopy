import sys
from itertools import *

n = [int(sys.stdin.readline().strip()) for _ in range(9)]

talls = list(permutations(n, 7))
for tall in talls:
    if sum(tall) == 100:
        print(*sorted(tall), sep="\n")
        break

'''
브론즈1
다시 풀어도 왜 최적화 방법을 모르겠지..
시간이 더 걸리게 풀었다.
처음 푼 코드 : barking/0x02/SevenDwarfs.py
'''