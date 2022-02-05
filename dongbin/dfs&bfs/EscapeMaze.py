# 미로 찾기 52:01
from collections import deque

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

# 상하좌우 좌표 setting
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y)) # 큐에 담기

    while queue: # 큐가 빌때까지 실행 -> 방문할 곳이 없을때까지
        x, y = queue.popleft() # 젤 왼쪽꺼 뽑아서 인접 노드 확인

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m: # 범위 벗어나면 pass
                continue
            if graph[nx][ny] == 0: # 0이면 pass
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1 # 거리 count

                if nx == n-1 and ny == m-1: # 맨 마지막 좌표면 끝!
                    return graph[n-1][m-1]
                else:
                    queue.append((nx, ny)) # 인접 노드 넣기

        graph[x][y] = 0 # 방문 처리 -> 방문 처리를 해줘야 다음 인접노드가 방문하지 않음
    return graph[n-1][m-1] # 맨 마지막 좌표 거리 반환

print(bfs(0, 0))
# print(graph)