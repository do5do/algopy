s1, s2 = input(), input()
a1, a2 = [0] * (ord('z') - ord('a') + 1), [0] * (ord('z') - ord('a') + 1) # 횟수 구할 배열 생성

for i in s1:
    a1[ord(i) - ord('a')] += 1
for j in s2:
    a2[ord(j) - ord('a')] += 1

cnt = 0
for i in range(len(a1)):
    if a1[i] != a2[i]: # 나온 횟수가 같으면 교집합
        cnt += abs(a1[i] - a2[i]) # 절댓값

print(cnt)