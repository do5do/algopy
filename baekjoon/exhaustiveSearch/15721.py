A, T, answer = [int(input().strip()) for _ in range(3)]

repeat, round = 0, 1
# 뻔 개수, 데기 개수
fcnt, dcnt = 0, 0
cnt, talk = 0, 0

flag = False
result = 0

while cnt < T:
    for i in range(A):
        if repeat <= 3: # 뻔 데기 뻔 데기
            if talk == 0: # 뻔
                fcnt += 1
                talk = 1
            else: # 데기
                dcnt += 1
                talk = 0
        else:
            for _ in range(round + 1):
                if talk == 0: # 뻔
                    fcnt += 1
                    talk = 0
                else: # 데기
                    dcnt += 1
                    talk = 1

                if i < A:
                    i += 1
                else:
                    i = 0

            if talk == 0: # 데기를 count하도록 바꿔줌
                talk = 1
            else:
                round += 1
                repeat = -1

        repeat += 1

        if answer == 0:
            cnt = fcnt
        else:
            cnt = dcnt

        if cnt == T:
            result = i
            flag = True
            break

    if flag:
        break

print(result)