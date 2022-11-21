import sys
from itertools import *
input = sys.stdin.readline

n = int(input().strip())
s = [list(map(int, input().strip().split())) for _ in range(n)]
num = [i for i in range(n)] # 조합을 구할 리스트
minValue = 200

combList = list(combinations(num, n//2)) # 반으로 나눈 수로 조합을 구함 -> 한 팀 설정
for comb in combList:
    start, link = 0, 0 # 팀 초기화
    other = [i for i in num if i not in comb] # 나머지 팀

    # 팀별 총 능력치 구하기
    for c in combinations(comb, 2): # 최소 2개(i,j)로 조합을 구함
        start += s[c[0]][c[1]] + s[c[1]][c[0]]

    for o in combinations(other, 2):
        link += s[o[0]][o[1]] + s[o[1]][o[0]]

    minValue = min(minValue, abs(start - link))

print(minValue)





