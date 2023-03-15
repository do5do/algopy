def solution(name):
    answer = 0
    alpha = {chr(i) : i - ord("A") + 1 for i in range(ord("A"), ord("Z") + 1)}
    move = len(name) - 1 # 커서 최대 이동

    for i in range(len(name)):
        # 커서 이동 없이 알파벳만 바꿔주기 (상하 이동 카운트)
        if alpha[name[i]] <= len(alpha) // 2 + 1:  # 앞에서부터 세기
            answer += (alpha[name[i]] - alpha["A"])
        else:  # 뒤에서부터 세기
            answer += 1 + (alpha["Z"] - alpha[name[i]]) # +1은 Z로 이동

        # 연속된 A 확인
        next = i + 1
        while next < len(name) and name[next] == "A":
            next += 1

        # 커서 이동 최소값 갱신 -> [A 상관없이 오른쪽으로만 이동, 연속된 A의 왼쪽 이동, 연속된 A의 오른쪽 이동]
        move = min([move, i * 2 + (len(name) - next), (len(name) - next) * 2 + i])

    return answer + move


print(solution("ABBAAAAAAAAAB"))


'''
조이스틱 level 2
- alphabet map 생성. key=alphabet, value=index
- 시작 알파벳은 무조건 A이다. (문제에 명시, 자리수 만큼)
- 뒤에서부터 세는게 빠른지 앞에서 부터 세는게 빠른지 확인
    - 알파벳 길이의 반을 나눠서 + 1 까지는 앞에서 세는게 빠르다.
- A를 만나면 왼쪽으로 이동하는게 빠른지 오른쪽으로 이동하는게 빠른지를 확인해야한다.
    - A는 건너뛰어도 되니 연속된 A를 찾아서 연속된 A를 제외하고, A를 만난 지점부터 왼쪽으로 이동한 것과 오른쪽으로 이동한 것 중 최소값으로 더해준다.
    - 연속된 A가 중간에 여러번 있는 경우까지 고려하여 루프를 돌며 최소값을 갱신해준다. 
=> 문제가 너무 헷갈렸다.. 커서 이동에 대해 문제를 제대로 안 읽어서 테이스케이스에 대한 답을 이해하는데 시간이 걸렸다.
(테스트케이스에 대한 정답에 대한 의견이 많이 갈려서 사실 뭐가 맞는지 정확하게 모르겠음)
커서 이동에 대한 핵심 풀이는 아래를 참고 했음.
https://velog.io/@jqdjhy/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%A1%B0%EC%9D%B4%EC%8A%A4%ED%8B%B1-Greedy
'''
