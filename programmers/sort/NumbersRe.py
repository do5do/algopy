def solution(numbers):
    numStr = list(map(lambda x: str(x).rjust(4, '0'), numbers))

    for i in range(len(numStr) - 1):
        for j in range(i+1, len(numStr)):
            for k in range(4):
                if numStr[i][k] < numStr[j][k]:
                    numStr[i], numStr[j] = numStr[j], numStr[i]

    # return "".join(map(lambda x: x.lstrip("0"), numStr))
    return "".join(map(str, map(int, numStr)))

# solution([6, 10, 2])
# print(solution([3, 30, 34, 5, 9]))
print(solution([1, 10, 100, 1000, 818, 81, 898, 89, 0, 0]))

'''
- 문자로 내림차순 정렬
- 문제는 30보다 3이 커야한다.
    - 각 자리수마다 비교 -> 30 vs 03
        - 최대 1000까지 이므로 앞에 0을 붙여 4자리 수를 만든다.
        - 선택 정렬을 사용하여 각 문자(char) 하나씩 비교하면서 내림차순 정렬했다. -> O(N) 시간초과!
    - 입력값이 0이면 모두 지워버린다. -> lstrip()으로 0을 지우는게 아니라 int로 바꿔주면 해결 된다.
=> 모르겠어서 정답을 봤다. 자리수를 비교할 새로운 풀이를 시도했고 답은 맞지만 시간 초과다..
'''