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
    if length == k - 5:
        cnt = 0
        for word in words:
            for w in word:
                # 각 단어가 배우지 않은거면
                if not learned[ord(w) - ord('a')]:
                    break
            else: # 위 for문의 else 구문. -> 각 단어를 모두 배웠으면 count
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
1. 필수 배울 단어를 미리 체크한다.
2. 모든 알파벳의 k-5의 개수만큼 조합으로 백트래킹 탐색
'''