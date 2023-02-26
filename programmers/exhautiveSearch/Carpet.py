def solution(brown, yellow):
    total = brown + yellow
    for i in range(3, total // 3 + 1):
        if total % i == 0:
            width = i
            height = total // i
            if (width * 2) + (height * 2) - 4 == brown and (width - 2) * (height - 2) == yellow:
                if width < height:
                    width, height = height, width
                return [width, height]

print(solution(8, 1))


'''
카펫 level 2
- 갈색은 최소 8 이상이기 때문에 가장 작은 수가 3이다.
- 갈색과 노란색을 합치면 총 수, 총 수로 나올 수 있는 배열을 하나씩 본다.
    - 3부터 총 수 // 3(= 최소 가로가 3이니까 총 수는 3*n이다.)까지 루프를 돌면서 총수를 나누어 나머지가 0일때만 확인한다.
        - brown = (가로*2) + (세로*2) - 4, yellow = (가로-2) * (세로-2)
        - 둘다 만족하는지 확인
- 가로는 세로보다 길다. -> desc 정렬해서 반환
=> 49분 소요. 풀이는 나름 빨리 구했다고 생각했는데 시간이 오래걸렸네..
'''