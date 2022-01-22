n, x = map(int, input().split()) # map(변환 함수, iterable)
num = list(map(int, input().split()))

for i in range(n):
    if num[i] < x:
        print(num[i], end=" ")