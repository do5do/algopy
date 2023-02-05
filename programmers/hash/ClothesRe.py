clothes = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
answer = 1 # answer를 곱할거니 1로 바꿔줌

clothDict = {}
# 각 종류 당 아이템이 몇개인지 구한다.
for item, kind in clothes:
    clothDict.setdefault(kind, 0) # key가 없으면 기본 값 0으로 설정
    clothDict[kind] += 1 # key가 있으면 value에 1을 더해 줌

# 종류 별 경우의 수를 구한다. ->  headgear1을 입는경우, headgear2를 입는경우, headgear를 모두 안입는 경우 = 총 3가지
for value in clothDict.values():
    # 종류별로 동시에 일어나는거니 곱의 법칙
    answer *= (value + 1)

# 종류별로 모두 안입는 경우는 없으니 모두 안입는 경우 1을 빼준다.
print(answer - 1)

'''
문제 풀이
- 각각 한 종류씩 입을 수도 있고 안 입을 수도 있다. 하지만 모두 안 입는 경우는 없다.
- 즉, headgear를 입는 경우와 안 입는 경우가 있고 eyewear를 입는 경우와 안 입는 경우가 있다.
    - headgear(2), eyewear(1)개일 때 headgear1을 입는 경우, headgear2를 입는 경우, headgear를 안 입는 경우로 총 headgear는 3가지다.
    - eyewear1을 입는 경우, eyewear를 안 입는 경우 = 2가지
    - headgear와 eyewear를 고르는 경우는 동시에 발생한다. => 곱의 법칙으로 3 * 2로 총 6가지 경우인데,
    여기엔 모두 안입는 경우(headgear 안 입는 경우, eyewear 안 입는 경우)가 포함되어 있다.
    - 하지만 모두 안입는 경우는 없으니 답은 6가지 중 모두 안입는 경우 1을 빼서 5가 된다.
'''