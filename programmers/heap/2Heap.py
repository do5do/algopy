import heapq


def solution(operations):
    heap = []

    for op in operations:
        ops = op.split()

        if ops[0] == "I": # insert
            heapq.heappush(heap, int(ops[1]))
        else: # delete
            if heap:
                if ops[1] == '1': # 최대값 삭제
                    heap.pop(heap.index(heapq.nlargest(1, heap)[0]))
                else: # 최소값 삭제
                    heapq.heappop(heap)

    if heap:
        return [heapq.nlargest(1, heap)[0], heap[0]]
    else:
        return [0, 0]

print(solution(["I 1", "I 2", "I 3", "I 4", "I 5", "I 6", "I 7", "I 8", "I 9", "I 10", "D 1", "D -1", "D 1", "D -1", "I 1", "I 2", "I 3", "I 4", "I 5", "I 6", "I 7", "I 8", "I 9", "I 10", "D 1", "D -1", "D 1", "D -1"]))

'''
이중우선순위큐 level 3
문제 풀이
- operations의 명령을 하나씩 수행한다.
- 힙을 만들어서 넣는데, 최대값을 삭제 하는 경우가 문제다.
    - 여러 방법을 생각해봤는데, 그냥 맨 뒤에꺼 뽑는거로 했다. 간단ㅎ
    - 마지막 6번 테케만 실패했다..
        - 위 테케 8,3이 정답인데 그냥 heap.pop()만 하면 답이 7,3이 나온다. 힙을 넣고 뺄때 정렬이 제대로 안된다.
            - 아하.. 힙은 이진 트리 자료 구조라서 sort를 한 것처럼 정렬이 되는게 아니다. 그래서 맨 마지막꺼가 가장 큰 값이 아닌 경우가 있는 것이다.
            - 그래서 nlargest를 찾아서 pop을 하면 가장 큰 값을 찾아서 뽑는 것이기 때문에 통과한다.
'''