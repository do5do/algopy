# 곱하기 혹은 더하기 문제 19:04
s = input()

result = int(s[0])

# 연산하는 두 수 중 하나라도 0 or 1이면 더하기 수행
for i in range(1, len(s)):
    item = int(s[i])
    if result <= 1 or item <= 1:
        result += item
    else:
        result *= item

print(result)
