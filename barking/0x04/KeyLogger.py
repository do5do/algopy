n = int(input())

for _ in range(n):
    result = []
    s = list(map(str, input()))
    cur = 0
    for i in s:
        if i == '<':
            if cur > 0:
                cur -= 1
        elif i == '>':
            if cur < len(result):
                cur += 1
        elif i == '-':
            if cur > 0:
                cur -= 1
                result.pop()
        else: # 입력
            if cur == len(result):
                result.append(i)
            else:
                result.insert(cur, i) # 시간 초과 O(N)
            cur += 1

    print("".join(result))