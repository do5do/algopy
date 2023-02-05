# 다시 풀기 : 2회차
def solution(clothes):
    answer = 1
    clothesDict = {}

    for cloth in clothes:
        clothesDict.setdefault(cloth[1], 1)  # 착용하지 않는 경우를 포함하여 default value를 1로 설정
        clothesDict[cloth[1]] += 1

    for val in clothesDict.values(): # 곱의 경우의 수 구함
        answer *= val

    return answer - 1 # 모두 착용하지 않는 경우 제외

print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))


'''
위장
문제 풀이
- 종류별로 경우의 수를 구한다.
    - headgear 2, eyewear1일때 각각 착용하지 않는 경우가 있다.
    - 착용하지 않는 경우까지 하면 headgear3, eyewear2가지이고 총 경우의 수는 3 x 2이다.
    - 여기서 모두 착용하지 않는 경우 1가지를 빼준다.
=> 풀이가 사실 생각안나긴 했다. 비슷한 문제를 다시 풀어봐야겠다. 30분 소요
'''