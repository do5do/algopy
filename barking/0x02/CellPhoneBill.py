n = int(input())
times = list(map(int, input().split()))
y = 0
m = 0

for time in times:
    y += time // 30 * 10 + 10
    m += time // 60 * 15 + 15

if y < m :
    print("Y", y)
elif y == m:
    print("Y M", y)
else:
    print("M", m)

