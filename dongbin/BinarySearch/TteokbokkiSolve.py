n, m = map(int, input().split())
tteok = list(map(int, input().split()))

start = 0
end = max(tteok)

result = 0
while start <= end:
    mid = (start + end) // 2
    total = 0
    for x in tteok:
        if mid < x:
            total += x - mid

    if total < m:
        end = mid - 1
    else: # total == mid, total > mid일때 모두 해당
        result = mid
        start = mid + 1

print(result)