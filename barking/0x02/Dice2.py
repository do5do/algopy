nums = sorted(list(map(int, input().split()))) # 오름차순 정렬하여 list에 담기
numsSet = set(nums) # 중복제거

money = 0
if len(numsSet) == 1: # 3개가 모두 같을때
    money = 10000 + nums[0] * 1000
elif len(numsSet) == 2:
    money = 1000 + nums[1] * 100 # 정렬을 하면 중간이 무조건 같은 수
else:
    money = nums[-1] * 100
print(money)