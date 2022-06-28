# 왕실의 나이트 48:32
place = input() # 좌표값 ex. a1
alpha = ['a','b','c','d','e','f','g','h']
x = int(place[1])
y = alpha.index(place[0]) + 1

# u d l r
xy = [[(-2,-1),(-2,1)],
      [(2,-1),(2,1)],
      [(-1,-2),(1,-2)],
      [(-1,2),(1,2)]]
cnt = 0
for i in range(len(xy)):
    x1 = x + xy[i][0][0]
    x2 = x + xy[i][1][0]
    y1 = y + xy[i][0][1]
    y2 = y + xy[i][1][1]
    if (x1 >= 1 and x1 <= 8) and (y1 >= 1 and y1 <= 8):
        cnt += 1
    if (x2 >= 1 and x2 <= 8) and (y2 >= 1 and y2 <= 8):
        cnt += 1

print(cnt)
