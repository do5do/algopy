# 음료수 얼려먹기 44:48
n, m = map(int, input().split())

# 2차원 리스트 생성
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

def dfs(i, j):
    # 해당 좌표 범위를 벗어나면 볼 필요 없음
    if i < 0 or i >= n or j < 0 or j >= m:
        return False

    if graph[i][j] == 0:
        graph[i][j] = 1 # 해당 노드 방문 처리

        # 상하좌우(인접 노드) 재귀 호출하여 방문 처리
        dfs(i-1, j)
        dfs(i+1, j)
        dfs(i, j-1)
        dfs(i, j+1)
        return True

    return False

cnt = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j):
            cnt += 1

print(cnt)