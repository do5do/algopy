import sys
N = int(sys.stdin.readline().strip())

visit = []
candy = []
for _ in range(N):
    # 2차원 배열 생성
    candy.append(list(map(str, sys.stdin.readline().strip())))
    visit.append([0] * N)

print(candy)
print(visit)

# 상하죄우 좌표
x = [-1, 1, 0, 0]
y = [0, 0, -1, 1]

def dfs(i, j):
    cnt = 1
    for n in range(4):
        dx = i + x[n]
        dy = j + y[n]
        if dx < 0 or dy < 0 or dx > N or dy > N:
            continue
        if visit[dx][dy] == 0:
            visit[dx][dy] = 1 # 방문 체크
            if candy[i][j] != candy[dx][dy]:
                # 노드 교환
                candy[i][j] = candy[dx][dy]
                candy[dx][dy] = candy[i][j]
                # 일직선 상에 같은게 몇갠지 체크?
            else:
                cnt += 1
                dfs(dx, dy)
        else:
            continue





dfs(0, 0)