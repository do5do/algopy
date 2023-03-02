from collections import deque




def solution(n, wires):
    answer = -1
    graph = [[] * (n + 1)]
    for a, b in wires: # graph 세팅 (모든 연결관계를 표시한다.)
        graph[a].append(b)
        graph[b].append(a)

    for a, b in wires:
        visited = [False] * (n+1)

    return answer


print(solution(4, [[1,2],[2,3],[3,4]]))


'''
전력망을 둘로 나누기 level 2 -> bfs 풀이
*bfs : 임의의 경로를 찾고 싶을때 사용. 방문한 노드들을 차례로 꺼낼 수 있는 큐를 사용한다.
'''