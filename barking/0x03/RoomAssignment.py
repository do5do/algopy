n, k = map(int, input().split()) # 총 학생수, 방 당 최대 인원수
li = [[0] * 7 for i in range(2)] # 2차원 배열 생성
cnt = 0
for i in range(n):
    s, y = map(int, input().split())
    li[s][y] += 1 # 나온 횟수 체크

for i in range(len(li)):
    for j in range(len(li[i])):
        cnt += li[i][j] // k
        if li[i][j] % k: # 나머지가 있으면 + 1
            cnt += 1

print(cnt)