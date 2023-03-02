def solution(n, wires):
    answer = -1
    tower = [set(), set()]
    for i in range(len(wires)):
        conn = dict()
        one, two = 0, 0
        for j in range(len(wires)):
            if j != i: # 연결 정보 하나씩 무시
                conn[wires[j][0]] = wires[j][1] # 연결 정보 저장
        print(conn)

        # for i in range(len(conn)): # 연결된 송전탑의 개수를 세기 위함
        #     if

        for t in tower:
            if t:
                one += 1
            else:
                two += 1


    return answer

print(solution(4, [[1,2],[2,3],[3,4]]))


'''
전력망을 둘로 나누기 level 2
- 주어진 연결을 하나씩 다 끊어본다.
    - 0번 연결 정보를 무시, n번까지 반복
- 각 연결 정보를 저장한다.
- 서로 연결이 되어 있으면 카운트 한다.? -> 구현 못함..
    - 연결 정보가 끊긴 시점에 카운트 저장하고 송전탑 개수의 차이를 절대값으로 저장한다.
- 개수의 차이 중 최소값 반환 
=> 감도 안잡혀서 힌트를 봤다. 연결정보를 하나씩 다 끊어본다는 것을 얻어냄
=> 1시간 정도 풀어봤는데 시간내에 구현을 다 못했다.
'''