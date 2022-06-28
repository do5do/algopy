# 모험가 길드 25:00
N = int(input()) # 모험가 수
fears = sorted(list(map(int, input().split()))) # 공포도

member = 0 # 인원수
group = 0 # 만들 수 있는 그룹의 수
for fear in fears:
    member += 1
    if member >= fear:
        group += 1
        member = 0

print(group)

