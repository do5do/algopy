tall = sorted([int(input()) for _ in range(9)])

flag = False
for i in tall:
    for j in tall:
        if i + j == sum(tall) - 100:
            tall.remove(i)
            tall.remove(j)
            flag = True
            break

    if flag:
        break

for i in tall:
    print(i)

