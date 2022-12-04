A, B, C, M = map(int, input().split())

tired = 0
work = 0
for time in range(1, 25):
    if tired <= M - A:
        tired += A
        work += B
    else: # 번아웃
        tired -= C
        if tired < 0:
            tired = 0

print(work)

'''
bronze 2
'''