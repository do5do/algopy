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
silver3, dynamic programming 문제
DP는 점화식을 잘 세워야 한다.
풀이: n = 4일 때, (합이 3인 경우의 수)+1과 (합이 2인 경우의 수)+2와 (합이 1인 경우의 수)+3을 더하면
합이 4인 경우의 수가 모두 도출된다. 즉, 점화식은 a[n] = a[n-1] + a[n-2] + a[n-3] 이렇게 된다.
'''
