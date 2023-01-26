from collections import deque

priorities = [2, 3, 3, 2, 9, 3, 3] # 중요도
location = 3
answer = 0

# index와 priority를 튜플로 가지는 덱 생성
queue = deque([(index, priority) for index, priority in enumerate(priorities)])

cnt = 0
while queue:
    maxPrior = max(queue, key=lambda x: x[1]) # 최대값은 계속 갱신 됨 (queue가 변하기 때문)
    pop = queue.popleft()
    if pop[1] == maxPrior[1]: # 첫번째 값과 최대값이 같을 때
        cnt += 1 # 출력
        if location == pop[0]: # location의 위치이면 cnt(출력 순서) 반환
            answer = cnt
            break
    else: # 최대값보다 작을 때
        queue.append(pop)  # queue의 맨 뒤에 입력

print(answer)

'''
프린터 level 2
문제 풀이
- priority의 인덱스를 알아야해서 (inx, priority)로 deque을 생성한다.
- 최대값을 구하여 첫번째 값과 비교하여 작은 값이면 뽑아서 뒤로 보내고,
- 최대값과 같은 값이면 출력한다. -> 출력 순서를 말함
    - 이때 출력할 요소가 찾던 값이면(location) 해당 출력 순서를 리턴한다.
'''