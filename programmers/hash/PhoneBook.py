phone_book = ["1235", "123", "12348", "012"]

answer = True
phone_book.sort() # 문자 마다 작은 숫자 순으로 정렬 (12348 < 1235)
for i in range(len(phone_book) - 1):
    if phone_book[i + 1].startswith(phone_book[i]):
        answer = False
        break

print(answer)

'''
전화번호 목록 level 2
문제 풀이
- 어떤 번호가 다른 번호의 접두어인지를 찾는 것이니까 먼저 비교해야하는 것은 길이가 짧은 전화번호이다.
    - 작은 숫자 순으로 정렬한다. (길이가 짧은 순이 아니라 각 문자 하나씩 비교해서 작은 순으로 매기는데 결국 인접한 것들 순으로 정렬된다.)
    - 순서대로 앞의 번호가 뒤에 있는지 탐색한다.
        - 이때 i in str 이라고 조건을 두면 안된다. 이건 접두어만 보는게 아니라 해당 문자열 내에 i가 있는지를 보는 것이다. 
'''