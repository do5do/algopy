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


print(solution("ABAAAAABAB"))
