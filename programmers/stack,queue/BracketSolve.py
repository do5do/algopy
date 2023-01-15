s = ")()("
answer = True

stack = []
for i in s:
    if i == '(':
        stack.append(i)
    else:
        if not stack: # s의 가장 처음 원소가 )일 때
            answer = False
            break
        else:
            stack.pop() # )의 짝을 제거 해줌

if stack: # 스택에 값이 있다는 것은 괄호의 짝이 맞아서 모두 제거되지 않았다는 의미.
    answer = False

print(answer)

'''
문제 풀이
- 괄호의 짝이 맞는지 확인하는 걸 너무 어렵게 생각했다.
    - (이 앞에 몊개가 있든 )가 나오면 바로 앞에 있는 (과 짝인 것.
    - 해당 (을 지워준다. -> 짝이 맞지 않으면 지워지지 않고 남아 있을테니 결과는 false이다.
- 위 과정을 스택이 아닌 카운트로 처리해도 방법은 같다.
    - open 카운트 변수 하나로 오픈이면 +1 클로즈이면 -1을 하는 형태로 처리하면 된다.

느낀점
이렇게 쉬운것을 왜... 처음에 생각하지 못했을까ㅠㅠ
'''