from collections import deque

# 반례 -> 6을 리턴해야 하는데, 아래 코드는 7을 리턴함
priorities = [2, 3, 3, 2, 9, 3, 3] # 중요도
location = 3
answer = 0

# index와 priority를 튜플로 가지는 덱 생성
queue = deque([(index, priority) for index, priority in enumerate(priorities)])

maxPrior = max(queue, key=lambda x: x[1])[1]
while queue:
    if queue[0][1] < maxPrior: # 최대값보다 작을 때
        queue.append(queue.popleft()) # 첫번째 원소 뽑아서 queue의 맨 뒤에 입력
    else: # 크거나 같을 때인데 클때는 없음 -> 최대값과 같을 때
        queue = sorted(queue, key=lambda x: x[1], reverse=True) # queue를 우선순위 순서대로 정렬
        break

# queue에서 location의 위치를 찾아서 리턴
for i in range(len(queue)):
    if queue[i][0] == location:
        answer = i + 1

print(answer)

'''
프린터 level 2
문제 풀이
- priority의 인덱스를 알아야해서 (inx, priority)로 deque을 생성한다.
- 최대값을 구하여 첫번째 값과 비교하여 작은 값이면 뽑아서 뒤로 보내고,
- 최대값과 같은 값이면 멈추고 중요도 내림차순으로 정렬한다.
    - 같은 수 일때는 정렬 전 리스트 순서를 유지하기 때문에 문제에서 요구하는 같은 값일 때 요구하는 순서와 맞을거라고 생각했다.
    - 하지만 위와같은 반례가 있다... 최대값인 9를 제외하였을 때 인덱스 3의 2는 인덱스 0의 2보다 먼저 출력되어야 한다.
=> 테케 반타작..!ㅜㅜ
'''