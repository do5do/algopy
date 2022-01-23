# 시각 42:47
hour = int(input())

# 3이 있는지 하나씩 확인하는 완전 탐색 문제
# python은 1초에 2천만번의 연산을 수행
cnt = 0
for i in range(hour + 1): # 시
    for j in range(60): # 분
        for k in range(60): # 초
            if '3' in str(i) + str(j) + str(k): # 시분초를 나열한 문자열 안에 3이 포함되어 있는지 확인
                cnt += 1

print(cnt)
