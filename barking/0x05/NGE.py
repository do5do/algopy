import sys
input = sys.stdin.readline
n = int(input())
nums = list(map(int, input().split()))
stack = []
result = [-1] * n

for i in range(len(nums)):
    while stack and nums[stack[-1]] < nums[i]:
        result[stack[-1]] = nums[i]
        stack.pop()
    stack.append(i)

print(*result)