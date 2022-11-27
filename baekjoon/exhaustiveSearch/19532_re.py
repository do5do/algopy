a, b, c, d, e, f = map(int, input().split())

flag = False
for i in range(-999, 1000):
    for j in range(-999, 1000):
        if a * i + b * j == c and d * i + e * j == f:
            print(i, j)
            flag = True
        if flag:
            break
    if flag:
        break

'''
bronze 2
교훈 : 흔히 방정식을 풀때 x, y를 소거하는데, 컴퓨터는 그럴 필요가 없다.
범위가 정해져있고 x,y는 유일하다고 문제에 나와있다. 무식하지만 for문으로 다 찾으면 되는구나..
또는 가감법을 사용한다. 
'''