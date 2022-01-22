tall = [int(input()) for _ in range(9)]

flag = False
for i in range(8):
    for j in range(i+1, 9):
        if sum(tall) - (tall[i] + tall[j]) == 100:
            one, two = tall[i], tall[j] # 변수에 안 담고 바로 지워버리면 tall[i]를 먼저 지워버리기 때문에 tall[j]의 값이 달라져 버림 (길이가 짧아져서 인덱스가 달라지기 때문)
            tall.remove(one)
            tall.remove(two)
            tall.sort()
            flag = True
            break

    if flag:
        break

for i in tall:
    print(i)