def solution(numbers):
    for number in numbers:
        for n in numbers:
            pass


# print(solution([3, 30, 34, 5, 9]))
# print(solution([0, 4, 0]))
# print(solution([123,1232]))
print(solution([1, 10, 100, 1000, 818, 81, 898, 89, 0, 0])) # 89/898/818/81/1/10/100/1000/0/0

'''
가장 큰 수 level 2
문제 풀이 1차
- numbers를 문자열로 바꿔서 정렬한다.
- 정렬한 리스트를 unpacking하여 리턴
    - unpacking이 안되네. join 하자
=> 반례가 매우 많고 조건을 어떻게 맞춰야할지 모르겠다...ㅠㅠ 어렵네?ㅜㅜ

2차

'''