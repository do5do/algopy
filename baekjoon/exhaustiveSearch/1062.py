import sys
import re
from itertools import *
input = sys.stdin.readline

n, k = map(int, input().strip().split())
default = 'a|n|t|i|c'
# default 제거
words = [re.sub(default, '', input().strip()) for _ in range(n)]
adds = set()
addCnt = k - 5
maxCnt = 0

def setAdds():
    for w in words:
        adds.update(set(w))

# adds에서 추가 단어의 수 만큼 선택 -> 만들 수 있는 단어의 최대 개수 탐색.
def find():
    global maxCnt

    # 조합 구하기
    comb = combinations(adds, addCnt)
    for com in comb:
        cnt = 0
        for word in words:
            for w in set(word):
                if w not in com:
                    break
            else: # 모두 들어 있을때만 count
                cnt += 1
        maxCnt = max(maxCnt, cnt)

setAdds()
if addCnt < 0: # 모두 배울 수 없을 때
    print(0)
elif addCnt == 21 : # 모두 배울 수 있을 때 (k가 소문자 알파벳 개수와 같을때)
    print(n)
else:
    find()
    print(maxCnt)

'''
시간 초과 (pypy로 제출 시 틀림..)
'''
