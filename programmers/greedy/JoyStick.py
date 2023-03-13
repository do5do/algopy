def solution(name):
    answer = 0
    alpha = {chr(i) : i - ord("A") + 1 for i in range(ord("A"), ord("Z") + 1)}
    print(alpha)

    maxMove = len(name) - 1 # 커서 최대 이동

    for n in name:
        # 커서 이동 없이 알파벳만 바꿔주기 (상하 이동 카운트)
        if alpha[n] <= len(alpha) // 2 + 1:  # 앞에서부터 세기
            answer += (alpha[n] - alpha["A"])
        else:  # 뒤에서부터 세기
            answer += 1 + (alpha["Z"] - alpha[n]) # +1은 Z로 이동

        # 커서 이동 확인



    return answer

print(solution("JAN"))
