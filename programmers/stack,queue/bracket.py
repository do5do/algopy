from collections import deque
answer = True
s = "(()("

queue = deque(list(s))

open = 0 # ( 의 개수
close = 0 # ) 의 개수
while queue:
    pop = queue.popleft()
    if pop == '(':
        open += 1
    else:
        close += 1
        if len(queue) >= 1:
            if pop != queue[0]:
                if open != close:
                    answer = False
                    break

print(answer)

'''
올바른 괄호 level 2
문제 풀이
- 괄호의 짝이 맞는지 확인하면 된다고 생각했다.
- 맨 앞 괄호를 뽑는다. ( 이면 카운트한다.
- 다음 괄호를 뽑고 같은거면 카운트를 올려주고, 
- 다른 거면 카운트끼리 비교해서 수가 다르면 짝이 맞지 않은거니 false
=> 1시간 시도, 실패(테케 반은 틀림)

느낀점
테스트 케이스를 모두 생각해서 풀이를 생각해내야 한다.
예외도 생각해야 한다. 테케 하나만 보고 풀이를 떠올리고 그게 맞다고 짜기 시작하면 그때부터 꼬이는거다.. 이렇게...
'''