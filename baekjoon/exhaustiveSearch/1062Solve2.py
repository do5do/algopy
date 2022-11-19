from itertools import *
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

def countWord():
    global maxCnt

    cnt = 0
    for word in words:
        for w in word:
            # 각 단어가 배우지 않은거면
            if not learned[ord(w) - ord('a')]:
                break
        else:  # 위 for문의 else 구문. -> 각 단어를 모두 배웠으면 count
            cnt += 1
    maxCnt = max(maxCnt, cnt)  # max 값 갱신

alpha = []
for i in range(0, 26):
    if chr(i + ord('a')) not in default:
        alpha.append(i)

for comb in combinations(alpha, k - 5):
    # 조합 learned check
    for c in comb:
        learned[c] = 1
    countWord()
    # learned 복구
    for c in comb:
        learned[c] = 0

print(maxCnt)

'''
combinations로 조합을 구하여 푼 방법. pypy3으로 제출
속도는 이게 더 빠르게 나왔다. (644ms)
교훈: itertools를 쓰는게 나쁜게 아니다. 시험에 맞을려면 나는 써야겠다.
대신 순서가 필요한지 아닌지를 고려해서 permutations를 쓸건지 combinations를 쓸건지 잘 생각해서 사용하자.
'''