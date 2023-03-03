from collections import deque


def bfs(visited, graph, start): # 연결된 노드를 탐색
    queue = deque([start])
    cnt = 1
    visited[start] = True
    while queue:
        top = queue.popleft()
        for i in graph[top]: # 연결된 노드가져와서
            if not visited[i]: # 방문한적이 없으면
                cnt += 1 # 연결된 것이니 개수를 센다.
                visited[i] = True
                queue.append(i)
    return cnt

def solution(n, wires):
    answer = n
    graph = [[] for _ in range(n + 1)]
    for v1, v2 in wires: # graph 세팅 (모든 연결관계를 표시한다.)
        graph[v1].append(v2)
        graph[v2].append(v1)

    for start, notVisit in wires:
        visited = [False] * (n+1)
        visited[notVisit] = True # 연결 정보 끊기
        v1Cnt = bfs(visited, graph, start)
        v2Cnt = n - v1Cnt # 전체에서 한쪽 전력망의 송전탑 개수를 빼면 남은 전력망의 송전탑의 수
        answer = min(abs(v1Cnt - v2Cnt), answer)
    return answer


print(solution(4, [[1,2],[2,3],[3,4]]))


'''
전력망을 둘로 나누기 level 2
*bfs : 임의의 경로를 찾고 싶을때 사용. 방문한 노드들을 차례로 꺼낼 수 있는 큐를 사용한다. (dfs로 푸는 것도 가능)
- 모든 연결관계를 가진 그래프를 생성해준다.
- 연결 정보를 하나씩 끊어서 전력망의 송전탑 개수를 알아낸다.
- 한쪽의 개수를 알아내고 전체에서 알아낸 개수를 빼면 다른 한쪽의 개수가 된다.
- 그 차이를 구해서 최소값을 반환한다.
=> bfs, dfs 많이 연습해야겠다,, 이 문제를 dfs로도 풀 수 있었다.
'''