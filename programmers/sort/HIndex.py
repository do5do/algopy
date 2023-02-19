def solution(citations):
    citations = sorted(citations, reverse=True)
    for i in range(len(citations)):
        if citations[i] <= i:
            return i
    return len(citations)

# print(solution([3, 0, 6, 1, 5]))
print(solution([100, 100, 100]))

'''
H-index level 2
- https://www.ibric.org/myboard/read.php?Board=news&id=270333 이 글을 보고 h-index를 이해했다.
- 인용수가 논문의 수(index)와 같거나 작아지기 시작하는 수가 h-index가 된다.
- 인용수를 내림차순 정렬하여 논문의 수(index)와 비교하여 같거나 작은 시점에 break
    - 9번 테캐만 실패하는데, h-index가 주어진 배열에 포함된 값이 아닐 경우를 고려하지 않음
        - [100, 100, 100]이면 인용수가 논문의 수보다 작거나 같은 수가 없기 때문에 최대값인 최대 논문 수를 리턴한다.
=> 문제 이해햐기 개 힘드네... 문제가 너무 이상하다ㅠ
'''