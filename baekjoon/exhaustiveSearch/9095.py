T = int(input())
arr = [0] * 11
arr[1] = 1
arr[2] = 2
arr[3] = 4


def recursive(n):
    if arr[n] != 0:
        return arr[n]
    else:
        arr[n] = recursive(n - 1) + recursive(n - 2) + recursive(n - 3)
        return arr[n]


for i in range(T):
    print(recursive(int(input())))

'''
silver3
dynamic programming 문제
DP는 점화식을 잘 세워야 한다.
a[i] = a[i-1] + a[i-2] + a[i-3]
오늘의 교훈: DP 문제라는 걸 어떤 걸 보고 구분할까?
많이 풀어보는게 답일거 같다.
'''
