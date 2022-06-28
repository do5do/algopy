# 왕실의 나이트 48:32
# 같은 접근법인데 나는 더럽게 구현했고 풀이는 간단하게 구현함,,
place = input() # 좌표값 ex. a1
x = int(place[1])
y = int(ord(place[0])) - ord('a') + 1 # ord() : ASCII code로 변환하는 함수

steps = [(-2,-1),(-2,1),(2,-1),(2,1),(-1,-2),(1,-2),(-1,2),(1,2)] # 8가지 방향
cnt = 0
for step in steps:
    nx = x + step[0]
    ny = y + step[1]
    if nx >= 1 and nx <= 8 and ny >= 1 and ny <= 8:
        cnt += 1

print(cnt)

