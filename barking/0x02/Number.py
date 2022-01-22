a,b = sorted(map(int, input().split()))
cnt = b - a -1
nums = [i for i in range(a+1, b)]
if b - a <= 1:
    cnt = 0
print(cnt)
print(*nums)
