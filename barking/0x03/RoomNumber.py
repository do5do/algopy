number = list(map(int, input()))
set = [0] * 9 # 0~8까지

for num in number:
    if num == 9:
        set[6] += 1
    else:
        set[num] += 1


if set[6] % 2 == 0:
    set[6] = set[6] // 2
else:
    set[6] = set[6] // 2 + 1

print(max(set))

# 다른 풀이
s = input()
n = [s.count(str(i)) for i in range(10)]
n[6] = n[6] + n[9] + 1 // 2
n[9] = n[6]
print(max(n))