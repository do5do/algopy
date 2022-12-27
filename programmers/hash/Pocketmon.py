nums = [3,3,3,2,2,4] # 포켓몬
# N/2 (몫)
answer = len(nums) // 2
if answer > len(set(nums)):
    answer = len(set(nums))

print(answer)

'''
포켓몬 level 1
문제 풀이
- 포켓몬 수의 절반을 구하면 그게 최대로 가져갈 수 있는 포켓몬 개수이다.
- 다만 포켓몬이 중복으로 있을 경우 포켓몬의 중복을 제거한 수가 절반의 수보다 작으면 그게 최대 값이다.
'''