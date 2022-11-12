import sys
input = sys.stdin.readline

n = int(input().strip())
candy = [list(input().strip()) for _ in range(n)]
visit = [[0]*n for _ in range(n)]

# 상하좌우 좌표
step = [[-1, 0], [1, 0], [0, -1], [0, 1]]
maxCnt = 0

def search():
    global maxCnt
    for i in range(n): # 행 count
        cnt = 1
        for j in range(n-1):
            if candy[i][j] == candy[i][j+1]:
                cnt += 1
                maxCnt = max(maxCnt, cnt)
            else:
                cnt = 1

    for i in range(n): # 열 count
        cnt = 1
        for j in range(n-1):
            if candy[j][i] == candy[j+1][i]:
                cnt += 1
                maxCnt = max(maxCnt, cnt)
            else:
                cnt = 1

for i in range(n):
    for j in range(n):
        for k in range(4):
            visit[i][j] = 1 # 방문 처리
            dx = i + step[k][0]
            dy = j + step[k][1]
            if dx < 0 or dy < 0 or dx >= n or dy >= n or visit[dx][dy]:
                continue
            if candy[i][j] != candy[dx][dy]:
                # swap
                candy[i][j], candy[dx][dy] = candy[dx][dy], candy[i][j]
                search()
                # swap 복구
                candy[dx][dy], candy[i][j] = candy[i][j], candy[dx][dy]

print(maxCnt)

'''
silver3
처음엔 어떻게 풀어야 하는지 감도 안와서 풀이를 찾아봤다.
제일 쉬운 방법은 현재 값의 인접 값 중 다른 값이면 스왑하고,
배열의 전체를 탐색하여 행열로 연속한 사탕의 수를 찾아서 max값에 갱신해준다.
(현재 코드에서 방문 처리를 하지 않으면 시간 초과)

속도 개선: swap을 굳이 하지 않고, 현재값의 오른쪽과 아래 값이 같으면 조건으로 검증할 수 있다.
'''