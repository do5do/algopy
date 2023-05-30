def solution(numbers):
    answer = ''
    numStr = sorted(map(str, numbers), reverse=True)
    print("".join(numStr))

    for num in numStr:
        s = num.rjust(4, "0")
        print(s)
    return answer

# solution([6, 10, 2])
solution([3, 30, 34, 5, 9])

'''
- 문자로 내림차순 정렬
    - 문제는 

'''