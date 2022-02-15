n = int(input())
arr = sorted(list(map(int, input().split()))) # 오름차순 정렬되어 있어야만 한다.
x = int(input())

check = [0] * 2000000
cnt = 0
for i in arr:
    if x > i and check[x - i] == 1: # x 가 i보다 클때에만 확인
        cnt += 1
    check[i] = 1

print(cnt)