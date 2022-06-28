n, m = map(int, input().split())
tteok = list(map(int, input().split()))

def findHeight(arr, start, end):
    mid = (start + end) // 2 # 높이
    rest = [0 if mid > x else x - mid for x in arr] # 잘린 값

    if start > end:
        return mid
    else:
        if sum(rest) == m:
            return mid
        elif sum(rest) > m:
            return findHeight(arr, mid + 1, end)
        else:
            return findHeight(arr, start, mid - 1)

print(findHeight(tteok, 0, max(tteok)))