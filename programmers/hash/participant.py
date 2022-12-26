participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]

# participant list를 dictionary로 변환.
partDict = {}
for i in participant:
    partDict.setdefault(i, 0) # default value는 0으로 설정한다.
    partDict[i] += 1 # key가 이미 있을 때(동명이인)는 count

for i in completion:
    partDict[i] -= 1

for key, value in partDict.items():
    if value != 0:
        print(key)

'''
문제 풀이
- 참가자를 dictionary로 변환한다.
    - 기본 값을 0으로 설정하고 동명이인이 있으면 기본 값에 1을 더해준다.
- 참가자 dict에서 완주자가 있으면 값에 1을 빼준다.
    - count(값)이 0이 아닌 사람이 완주하지 못한 사람이다.
- 완주하지 못한 사람은 무조건 한명 (문제 조건)
'''