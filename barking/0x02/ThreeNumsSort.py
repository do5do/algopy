import time
nums = list(map(int, input().split()))
startTime = time.time()
min = min(nums)
max = max(nums)
middle = sum(nums) - min - max
print(min, middle, max)
endTime = time.time()
print("time :", endTime - startTime) # 단위는 초

# wow...
# print(*sorted(map(int, input().split())))
