from collections import deque


def solution(bridge_length, weight, truck_weights):
    time = 0
    trucks = deque(truck_weights) # 대기 중인 트럭
    bridge = deque([0] * bridge_length)
    bridgeWeight = 0

    while bridge:
        time += 1
        bridgeWeight -= bridge.popleft() # 1초에 한칸씩 다리를 이동

        if trucks:
            if bridgeWeight + trucks[0] <= weight: # 다리에 다음 트럭을 올릴 수 있으면
                truck = trucks.popleft()
                bridge.append(truck) # 다리에 트럭 추가
                bridgeWeight += truck
            else:
                bridge.append(0) # 다리 길이 유지 = 칸 이동 없음 (공기만 보낸다.)

    return time


print(solution(2, 10, [7,4,5,6]))

'''
문제 풀이
- 트럭은 1초에 한칸씩 이동한다.
ex) 0 [][] [7,4,5,6]
    1 [][7] [4,5,6]
    2 [7][] [4,5.6]
    3 [][4] [5,6]
    4 [4][5] [6]
    5 [5][] [6]
    6 [][6] []
    7 [6][] []
    8 [][] [] # 모두 이동 완료
- 한 칸을 이동하는 것을 다리 길이를 한 칸 줄인다고 생각한다.
- 다리의 무게를 확인해서 무게보다 작거나 같으면 트럭을 추가한다.
- 무게보다 크면 다리 길이를 유지한다.

=> sum()을 사용하면 5번 히든 테케에서 시간초과가 난다.
    - sum()의 시간복잡도는 O(N)이기 때문. 무게를 직접 더하고 빼준다.
    - 어라.. sum()을 빼줘도 5번 통과가 안된다.
    - bridge를 deque에서 list로 바꿔주고 pop(0)을 하니까 통과된다.. list의 pop(index)는 느린걸로 알고 있는데 왜지?
'''