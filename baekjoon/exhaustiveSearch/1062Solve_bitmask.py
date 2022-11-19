from itertools import *
n, k = map(int, input().split())

if k < 5: # 아무것도 배울 수 없음
    print(0)
    exit() # 이거 안 해주면 여기서 안 멈추고 아래 줄 다 실행.
elif k == 26: # 모두 배울 수 있음
    print(n)
    exit()

default = ['a', 'n', 't', 'i', 'c']
words = [set(input()).difference(set(default)) for _ in range(n)] # default 제거

alpha = []
for i in range(26):
    if chr(i + ord('a')) not in default:
        alpha.append(i) # default 빼고 담기

maxCount = 0
for comb in combinations(alpha, k - 5):
    mask = 0
    for c in comb:
        mask |= 1 << c # fix = fix | (1 << c) : 1을 c만큼 이동 -> c 위치를 1로 만듬

    cnt = 0
    for word in words:
        bits = 0
        for w in word:
            bits |= 1 << ord(w) - ord('a') # 우선순위 -, <<, | 순서
        if mask | bits == mask: # mask | bits로 합치기 (둘의 1의 위치가 같은지 확인)
            cnt += 1
    maxCount = max(maxCount, cnt)

print(maxCount)

'''
bitmask로 푼 방법, pypy3으로 제출.
bitmask보다 배열로 푼 방법이 훨씬 빠르다.
비트마스크는 옮겨야 하는 수가 커질 수록 시간이 오래 걸려서 느린거라고 예상 
'''