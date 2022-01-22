def result(cnt):
    if cnt == 1:
        print('A') # 도
    elif cnt == 2:
        print('B')
    elif cnt == 3:
        print('C')
    elif cnt == 4:
        print('D') # 윷
    else:
        print('E') # 모

lists = []
for i in range(3):
    lists.append(list(map(int, input().split())))
# print(lists)

for list in lists:
    cnt = list.count(0) # 0의 개수를 세는 함수. 타입이 int일 경우만 가능하다.
    result(cnt)

