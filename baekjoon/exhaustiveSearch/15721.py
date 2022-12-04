A, T, inputs = [int(input().strip()) for _ in range(3)]

repeat, round = 1, 1
# 뻔 개수, 데기 개수
fcnt, dcnt = 1, 0
cnt, talk = 0, 0

flag = False
result = 0

while cnt < T:
    for i in range(1, A):
        repeat += 1
        if repeat <= 4: # 뻔 데기 뻔 데기
            if talk == 0:
                talk = 1
                dcnt += 1
            else:
                talk = 0
                fcnt += 1
        else:
            for _ in range(round + 1):
                if talk == 0:
                    talk = 0
                    fcnt += 1
                else:
                    talk = 1
                    dcnt += 1
                i += 1

        if inputs == 0:
            cnt = fcnt
        else:
            cnt = dcnt

        if cnt == T:
            result = i
            flag = True
            break

    round += 1

    if flag:
        break

print(result)