from itertools import permutations


def setNumber(nums):
    number = ""
    for n in nums:
        number += n
    return int(number)


def solution(numbers):
    answer = set()
    numbers = list(map(str, numbers))

    # 한자리 수 체크
    for n in numbers:
        n = int(n)
        if n == 2 or n == 3 or n == 5 or n == 7:
            answer.add(n)

    # 한자리 수 이상 체크
    for i in range(2, len(numbers) + 1):
        permut = set(permutations(numbers, i))

        for p in permut:
            if p[0] != '0':
                num = setNumber(p)
                for k in range(2, num): # 2부터 10까지가 아니라 2부터 num - 1까지 나눴을때를 확인해야 한다. => 수정하니 나머지 테케 통과
                    if num % k == 0:
                        break
                else:
                    answer.add(num)
    answer = sorted(answer)
    return len(answer)

print(solution("1231")) # 18이 답

'''
소수 찾기 level 2
- 입력받은 숫자의 조합을 구해서 1부터 9까지 다 나눠본다?
- 조합은 어떻게 구할까? 두 자릿수부터 numbers의 길이만큼의 자릿수까지 모두 구해야한다. 수가 커지면 어마어마할텐데..
    - 첮번째는 permutations를 쓰는 방법. (순서가 있는 순열)
    - 두번째는 직접 구한다. 뒤가 2,4,5,6,8,0 인것은 제외 (확실한거만 뺀다) -> 망함. 못 구함.
=> 반타작이네..
=> 소수 구하는 부분을 수정하니 통과했다. 소수가 뭔지 정확하게 알고있자.
'''