# 문자열 재정렬 52:33
s = input()
result = []
sum = 0

for i in s:
    if i.isalpha(): # isalpha() : 알파벳이면 true 아니면 false를 반환하는 내장 함수
        result.append(i)
    else:
        sum += int(i)

# 알파벳 오름차순 정렬
result.sort()

if sum != 0: # 숫자가 있으면 reault의 가장 마지막에 추가
    result.append(str(sum))

print(''.join(result))