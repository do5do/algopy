import copy

s1 = sorted(input())
s2 = sorted(input())
# alpha = [0] * (ord('z') - ord('a') + 1)

if s1 == s2:
    print(0)
else:
    tempS1 = copy.deepcopy(s1) # 깊은 복사
    for i in s2:
        if i in s1:
            s1.remove(i)

    for j in tempS1:
        if j in s2:
            s2.remove(j)
    print(len(s1+s2))



