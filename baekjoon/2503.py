from itertools import *

n = int(input())
nums = [list(map(int, input().split())) for _ in range(n)]

# 1~9까지 순서가 있는 모든 경우의 수를 구한다. (순열)
data = permutations([i for i in range(1, 10)], 3) # tuple로 반환 됨 [(1, 2, 3), ...]
result = []

for d in data:
    check = [False] * n
    for i in range(n):
        strike, ball = 0, 0
        numsStr = str(nums[i][0])
        for j in range(3):
            if str(d[j]) in numsStr:
                if str(d[j]) == numsStr[j]:
                    strike += 1
                else:
                    ball += 1

        if nums[i][1] == strike and nums[i][2] == ball:
            check[i] = True

    if False not in check:
        result.append(d)

print(len(result))

'''
오늘의 교훈:
나는 모든 데이터(1~9의 순열)를 각 nums마다 체크했는데 그럴 필요가 전혀 없었다... (난 바보ㅠ)
nums의 첫번째 요소에서 통과한 순열만 두번째 요소에서 검증하고, 거기서 통과(첫, 둘 모두 통과)한 순열만 세번째에서 검증
이런 방식으로 검증해야 할 순열의 리스트 개수를 줄여나간다면 시간이 엄청 빨라질 것 이다. -> O(N)에서 O(logN)정도? input num에 따라 더 빠를 듯 O(1)까지
'''