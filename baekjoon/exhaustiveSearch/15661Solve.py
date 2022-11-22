import sys
from itertools import *
input = sys.stdin.readline

# 사람 수
n = int(input().strip())
# 사람 별 능력치 matrix (자기 자신은 0)
matrix = [list(map(int, input().strip().split())) for _ in range(n)]

# 인당 능력치의 합 -> 1번의 능력치 합은 1번 row + 1번 column
manCap = []
for i in range(n):
    col = 0
    for j in range(n):
        col += matrix[j][i]
    manCap.append(sum(matrix[i]) + col)

# 총 능력치 (모든 능력치의 합)
totalCap = 0
for i in matrix:
    totalCap += sum(i)

# 팀 나누기 (한 팀에 한명 이상)
minValue = sys.maxsize
for i in range(1, n // 2 + 1):
    # start팀 조합 구하기
    for start in combinations(manCap, i):
        # (총 능력치 - start팀 능력치 합)으로 차이를 갱신
        minValue = min(minValue, abs(totalCap - sum(start)))
        if minValue == 0:
            break
    if minValue == 0:
        break

print(minValue)

'''
드디어 깔끔하게 이해 됐다.
matrix라는 걸 왜 이제 알았을까ㅠㅠ 하...
첫번째 맞았습니다는 맞은 사람들의 풀이 중 이해할 수 있는 풀이를 찾기 위해서 였다.
'''