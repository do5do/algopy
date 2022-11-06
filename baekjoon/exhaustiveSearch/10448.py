n = int(input())
triangle = [i*(i+1)//2 for i in range(1, 1000) if i*(i+1)//2 <= 1000]

eureka = set() # 세 원소의 합에는 중복이 있음
for i in triangle:
    for j in triangle:
        for k in triangle:
            sums = i + j + k
            if sums <= 1000:
                eureka.add(sums)

for i in range(n):
    result = 0
    num = int(input())
    if num in eureka:
        result = 1
    print(result)

'''
level: 브론즈1
브론즈1인데 겁나 틀렸다.
삼각 함수의 세 합에는 중복이 있다. 그리고 세 합은 1000이하만 찾으면 된다.
'''