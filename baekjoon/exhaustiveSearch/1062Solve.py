n, k = map(int, input().split())

if k < 5: # 아무것도 배울 수 없음
    print(0)
    exit()
elif k == 26: # 모두 배울 수 있음
    print(n)
    exit()

words = [input()[4:-4] for _ in range(n)]
default = ['a', 'n', 't', 'i', 'c']
learned = [0] * 26
for i in default: # 필수 배움
    learned[ord(i) - ord('a')] = 1

maxCnt = 0

def backtraking(alph, length):
    global maxCnt
    if length == k - 5: # 몇개 읽을 수 있는지 체크
        cnt = 0
        for word in words:
            for w in word:
                # 각 단어가 배우지 않은거면
                if not learned[ord(w) - ord('a')]:
                    break
            else: # 각 단어를 모두 배웠으면 count
                cnt += 1
        maxCnt = max(maxCnt, cnt) # max 값 갱신
        return # 없으면 끝나지 않음

    for i in range(alph, 26): # alphabet 하나씩 가르침
        if not learned[i]:
            learned[i] = 1 # 배움
            backtraking(i, length + 1) # 모든 조합을 확인할 수 있도록 재귀 호출
            learned[i] = 0 # 다시 원복

backtraking(0, 0)
print(maxCnt)

'''
gold4
python 제출 시간 초과, pypy3으로 제출 시 성공 (680ms)
'''