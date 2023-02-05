import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville) # heap 정렬 (heaq는 기본적으로 min heap)

    while len(scoville) >= 2:
        root = heapq.heappop(scoville) # root node 가져오기

        if root >= K: # root node가 K보다 크거나 같으면
            return answer
        else:
            newScoville = root + (heapq.heappop(scoville) * 2)
            heapq.heappush(scoville, newScoville) # 새로 계산한 스코빌 값 push하여 힙 정렬
            answer += 1

    if scoville[0] < K: # K이상으로 만들 수 없는 경우
        answer = -1
    return answer

# print(solution([1, 2, 3, 9, 10, 12], 7))
print(solution([1, 2, 3, 9, 10, 12], 300))


'''
더 맵게 level 2
문제 풀이
- 스코빌 지수에서 가장 낮은 수와 두번째로 낮은 수를 구하여 지문에 있는 식으로 값을 구하여 scoville에 넣고, 카운트 +1을 한다.
- 스코빌 리스트에서 가장 낮은 수를 가져와 K보다 크면 count를 리턴한다.
    - heap으로 구현
=> 25분 소요
'''