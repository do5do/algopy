# 상하좌우 37:48
N = int(input())
routs = input().split() # str이면 굳이 map에 담지않아도 됨.

x, y = 1, 1
# L R U D 순으로 세팅
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move = ['L', 'R', 'U', 'D']
nx, ny = 0, 0

for rout in routs:
    for i in range(len(move)):
        if rout == move[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    if nx < 1 or ny < 1 or nx > 5 or ny > 5:
        continue
    x, y = nx, ny

print(x,y)


