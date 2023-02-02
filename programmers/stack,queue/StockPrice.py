def solution(prices):
    answer = []

    for i in range(len(prices)):
        for j in range(i + 1, len(prices)):
            if prices[i] > prices[j]: # 주식 가격이 떨어지면
                answer.append(j - i) # 초 수 입력
                break
            else:
                if j == len(prices) - 1: # 가장 마지막 일 때
                    answer.append(j - i)
    answer.append(0) # 맨 마지막은 무조건 0
    return answer

print(solution([1, 2, 3, 2, 3]))

'''
주식가격 level 2
문제 풀이
- 하나씩 비교하면서 비교 수보다 작은 수가 있는지 확인 한다.
    - 초 수는 뒤 원소 인덱스에서 앞 원소 인덱스를 뺀다.
    - 작은 수가 나오면 answer에 초 수를 입력
    - 작은 수가 아니고 prices의 마지막이면 초 수를 입력
    - 이중 포문을 먼저 써보자
=> 23분만에 해결.. 레벨2가 너무 쉬운데? 믿기지 않네. O(N^2)이라 효율성에서 실패할줄 알았는데 괜찮네
'''