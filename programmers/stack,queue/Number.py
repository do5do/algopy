from collections import deque
arr = [4,4,4,3,3,4,4]
answer = []

queue = deque(arr)
while True:
    if len(queue) == 1:
        answer.append(queue[0]) # 마지막 남은 값 append
        break
    if queue[0] != queue[1]: # 첫번째 값과 다음 값으로 값 두개씩 비교
        answer.append(queue[0]) # 서로 다른 값일 때 append (== 앞에 같은 값을 모두 제거하고 남은 하나의 값을 넣는 것)
    queue.popleft() # 첫번째 값은 비교 후 뽑는다.

print(answer)

'''
같은 숫자는 싫어 level 1
문제 풀이
- 현재 값과 다음 값이 같은지 확인.
    - 값이 다를 때 answer에 넣어준다. (이게 핵심)
        - 처음엔 현재 값과 다음 값이 같을 때 answer에 넣어 줬는데,
        - 뒤에 또 같은 값이 나올 수 있기 때문에 값이 다를 때 answer에 넣는다.
- queue를 사용하여 현재 값과 다음 값을 비교하고 무조건 첫번째 값을 빼서 버린다.
    - 그래야 다음 첫번째 값과 그 뒤 값을 비교할 수 있다. => 두개씩 비교
=> 1시간 걸림... 그래도 마지노 시간안에 풀긴했다ㅠㅠ
'''



