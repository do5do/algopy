from itertools import product


def solution(word):
    dic = []
    for i in range(1, 6):
        pro = list(product(['A', 'E', 'I', 'O', 'U'], repeat=i))
        for p in pro:
            dic.append("".join(p))
    dic.sort()
    return dic.index(word) + 1

print(solution("AAAE"))


'''
모음 사전 level 2
- 모든 조합을 구한다.
    - 중복이 돼야하니 product를 사용한다.
- 순서대로 정렬한다.
- 해당 단어의 인덱스를 찾는다.
=> 모르겠어서 찾아봤다. 처음봤을때 조합을 구하는걸 쓸수 없을 줄알았는데 내가 문제를 제대로 이해하지 못해서 그랬던 것 같다.
'''