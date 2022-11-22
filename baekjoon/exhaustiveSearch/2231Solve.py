n = int(input())
rangeMin = max(1, n - (len(str(n)) * 9))
result = 0

for i in range(rangeMin, n):
    if i + sum(map(int, str(i))) == n:
        result = i
        break

print(result)

'''
최소 시작 범위: x + x의 자릿수 합이 분해합이다. -> 최소 범위를 구하려면 x에서 자리수 합의 최대값을 빼준다.
-> 자리수의 최대 수는 9, 자리수 합의 최대값은 자리수 만큼 9를 더한 것.
'''