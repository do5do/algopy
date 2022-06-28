n, k = map(int, input().split())
left = sorted(list(map(int, input().split())))
right = sorted(list(map(int, input().split())), reverse=True)

for i in range(k):
    if left[i] < right[i]:
        left[i], right[i] = right[i], left[i]
    else: # left의 원소가 right의 원소보다 크거나 같을때 반복문 탈출
        # => left, right는 정렬한거기에 크거나 같은 순간 left의 해당 원소보다 더 큰 수는 right에 없기때문에 그대로 반복문을 빠져나오는 것
        break

print(sum(left))
