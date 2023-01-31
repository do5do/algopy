from collections import deque


def solution(bridge_length, weight, truck_weights):
    time = 1
    trucks = deque(truck_weights)
    queue = deque() # 첫번째 트럭 달리기 시작

    while trucks:
        queue.append(trucks.popleft())
        while queue:
            if trucks:
                if sum(queue) + trucks[0] <= weight:
                    queue.append(trucks.popleft())
            time += 1

            if time % bridge_length == 0:  # 시간이 다리 길이만큼 흘렀으면 (= 다리를 건넌 것)
                queue.popleft()
    return time

print(solution(100, 100, [10,10,10,10,10,10,10,10,10,10]))

'''
다리를 지나는 트럭 level 2
문제 풀이
- 시간을 세자
    - 첫번째 트럭을 큐에 넣는다.
    - 큐의 sum과 다음 트럭을 더했을 때 weight 보다 작거나 같으면 큐에 추가한다.
    - 시간을 1씩 더해준다.
    - 시간이 bridge_length 만큼 흘렀으면 (time%length == 0) 큐 맨앞 원소를 뺀다.
    - 큐가 빌때까지 반복한다.
=> 주어진 테스트케이스도 다 통과하지 못함. 1시간 57분이나 걸렸다ㅠ 
'''