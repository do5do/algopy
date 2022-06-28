n, k = map(int, input().split())
left = sorted(list(map(int, input().split())))
right = sorted(list(map(int, input().split())), reverse=True)

for i in range(k):
    left[i] = right[i]

print(sum(left))

# 원소를 바꿔줄때 left의 원소가 right의 원소보다 작을때에만 교체하는걸 안함
# 시간초과가 일어날 수 있기때문에, O(NLogN)을 보장하는 정렬 알고리즘을 이용해야한다.
# -> 보통 표준 정렬을 이용하면 어떤 경우에도 O(NLogN)이 보장되도록 설계되어 있기때문에, 제공하는 표준 알고리즘을 사용하면 된다.
