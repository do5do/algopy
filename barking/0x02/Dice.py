nums = list(map(int, input().split())) # list에 담기
dict = {}
for num in nums:
    dict[num] = dict.setdefault(num, 0) + 1
# print(dict)

money = 0
for key, value in dict.items():
    if value == 3: # 같은 눈이 3개
        money = 10000 + key * 1000
        break
    elif value == 2: # 같은 눈이 2개
        money = 1000 + key * 100
        break
    else:
        money = max(nums) * 100

print(money)


