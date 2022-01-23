# 문자열 재정렬 52:33
import re

s = input()
st = sorted(re.findall('\D', s)) # 문자만 찾아서 오름차순 정렬
num = sum(map(int, re.findall('\d', s))) # 숫자만 찾아서 합 구하기

# for s in st:
#     result += s
# result += str(num)
result = "".join(st)
if num != 0: # 숫자가 없는 경우는 0이 추가 됨. 이를 방지하기 위해
    result += str(num)

print(result)
