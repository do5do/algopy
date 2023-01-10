answer = []
genres = ["classic", "pop", "classic", "classic"]
plays = [150, 600, 150, 800]

sumDicts = {} # 장르별 플레이 수 합 -> "pop" : 3100
itemDicts = {} # 장르별 인덱스, 플레이 수 -> "pop" : [(plays, index), ...]
for i in range(len(genres)):
    sumDicts.setdefault(genres[i], 0)
    sumDicts[genres[i]] += plays[i]

    itemDicts.setdefault(genres[i], [])
    itemDicts.get(genres[i]).append((plays[i], i))

# 플레이 수가 많은 순(value 순)으로 정렬
sumDicts = dict(sorted(sumDicts.items(), key=lambda x:x[1], reverse=True))

for kind in sumDicts.keys():
    # item을 플레이 순으로 정렬 (플레이 수가 같으면 인덱스가 작은게 앞으로 정렬되어야 함 -> 첫 입력 순서를 변경하면 안됨)
    sortedItems = sorted(itemDicts.get(kind), key= lambda x:x[0], reverse=True)
    length = len(sortedItems)
    if len(sortedItems) > 2: # 장르별 최대 두곡까지만 수록한다.
        length = 2
    for i in range(length):
        answer.append(sortedItems[i][1])

print(answer)

'''
베스트 엘범 level 3
문제 풀이
- 장르별 플레이 수를 먼저 확인한다.
    - 장르별 플레이 수 합을 value로 dict 생성, 플레이 수가 많은 순으로 내림차순 정렬한다.
- 플레이 수가 높은 장르 먼저 싣는다.
    - 장르별 플레이 수와 인덱스를 튜플 value로 dict 생성, 플레이 수 순으로 내림차순 정렬한다.
- 장르별 최대 두곡까지만 수록한다.
    - 수록 시 length 지정
=> 좋은 방법은 아니지만 풀긴했다! (총 2시간 걸림,,)
=> 다른 사람의 풀이를 보니 생각의 방향은 맞다. 코드를 축약하느냐의 차이.
'''

