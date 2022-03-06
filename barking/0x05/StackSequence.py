import sys

n = int(sys.stdin.readline())
nums = []
result = []
prevs = []
prev = 0
stack = []
flag = False

for _ in range(n):
    nums.append(int(sys.stdin.readline().strip()))

for num in nums:
    for i in range(prev + 1, num + 1):
        stack.append(i)
        result.append("+")
    temp = stack.pop()
    if temp == num:
        result.append("-")
    else:
        flag = True

    prevs.append(num)
    prev = max(prevs)

if flag:
    print("NO")
else:
    print("\n".join(result))

# 풀이는 맞는데 시간초과 => prev를 구하는데 시간복잡도가 O(NlogN). 이 부분을 바꾸면 가능할듯