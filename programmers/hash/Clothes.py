from itertools import combinations
clothes = [["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]
clothDict = {}
for i in clothes:
    clothDict[i[0]] = i[1] # key는 아이템 이름, value는 종류

# 조합 구하기 -> 조합의 수는 1부터 clothes 개수 만큼 각각 구한다.
combiLength = 0 # answer
for i in range(1, len(clothes) + 1):
    if len(set(clothDict.values())) == 1: # 모두 한 종류이면
        combiLength = len(clothes) # return answer
        break

    combi = list(combinations(clothDict.values(), i))
    combiLength += len(combi)
    for j in combi:
        if len(set(j)) != len(j): # 중복된 값을 찾아서 빼준다. (해당 조합에 중복된 종류가 있는지 확인)
            combiLength -= 1

print(combiLength)

'''
위장 level 2
문제 풀이
- 모든 아이템의 조합을 구한 다음에, 조합 중에 종류가 같은게 중복되어 들어 있으면 빼준다.
- 애초에 종류가 모두 같을 때는 clothes 길이만 세주면 된다.
=> 몇몇 테스트케이스에서 시간초과가 난다.
'''