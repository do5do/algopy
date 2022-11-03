n = int(input())
result = 0
for i in range(1, n):
    min = i
    for num in str(i):
        min += int(num)
    if min == n:
        result = i
        break

print(result)

'''
오늘의 교혼: 나는 브론즈2도 틀린다. 문제를 잘 읽자.. 없는 경우도 있다는걸 봤지만 고려하지 않아서 틀렸다.ㅠㅠ
파이썬의 장점을 잘 활용하자! 그리고 최소값을 구하려고 조금만 더 생각했더라면 시간 최적화를 할 수 있었을까?
최소 시작 범위를 못구한다고 생각해서 1이라고 뒀는데 시간이 매우 오래걸렸다.
(최적화 코드는 solution에 구현)
'''