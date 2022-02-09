multi = 1
num = [0] * 10

for i in range(3):
    multi *= int(input())

for m in str(multi):
    num[int(m)] += 1

for i in num:
    print(i)


# 다른 풀이
d=input
a=int(d())*int(d())*int(d()) # 개행으로 구분 되어짐
for j in range(10):
    print(str(a).count(str(j))) # count() : 개수를 세어주는 함수