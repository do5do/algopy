def solution(answers):
    answer = []
    correct = [0] * 3
    one = [1, 2, 3, 4, 5] * 10000
    two = [2, 1, 2, 3, 2, 4, 2, 5] * 10000
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * 10000

    for i in range(len(answers)):
        if answers[i] == one[i]:
            correct[0] += 1
        if answers[i] == two[i]:
            correct[1] += 1
        if answers[i] == three[i]:
            correct[2] += 1

    top = max(correct)
    for i in range(3):
        if correct[i] == top:
            answer.append(i + 1)
        return answer

print(solution([1,3,2,4,2]))

'''
모의고사 level 1
- answers의 길이에 맞춰서 각각의 답을 구해놓는다.
    - 이렇게 할랬는데 어차피 10000개가 최대니 그냥 만개 곱해서 최대치로 만들었다.
    - 이걸 순환주기로 나눠주는 방법이 있었다. -> answers[i] == one[i % len(one)] -> len(one)이 순환주기
=> 20분 소요. 이제 순환하면 순환주기를 생각하자! 디폴트로 박지말고,,
'''