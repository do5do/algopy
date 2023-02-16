def solution(numbers):
    numbers = list(map(str, numbers))
    numbers = sorted(numbers, key=lambda x: x * 3, reverse=True)
    return str(int("".join(numbers)))

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
- numbers의 요소는 1000이하의 정수이니 각 요소의 문자를 3번 곱한다. -> 최대 세자리 수까지 나오는데 각 자리마다 비교하기 위해 3을 곱한다.
    - 자리수를 맞출거면 뒤에 0을 붙여서 세자리 수를 만들면 안되나 생각했는데, 그럼 3과 30이 같아진다. -> 비교 불가
- 그리고 000이 나왔을 경우 0으로 반환하기 위해 숫자로 바꿔주고 return형은 문자열이기때문에 문자로 다시 바꿔준다.
=> 이런 생각 어떻게 하는거지...
'''