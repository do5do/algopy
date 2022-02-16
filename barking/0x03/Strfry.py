N = int(input())

for _ in range(N):
    s1, s2 = map(str, input().split())
    s1 = sorted(s1)
    s2 = sorted(s2)
    print('Possible' if s1 == s2 else 'Impossible')



# 처음 푼 코드인데 fail이다.
# s1의 원소 하나씩 a2에 있는지 비교함. 없는게 있으면 Impossible 출력
# 반례 -> aa aacc가 Possible이 나옴. 길이 체크를 안해줬기때문이라고 생각했는데 길이 체크 해줘도 왜 fail??
# 반례 -> aab abc인 경우 Possible

# N = int(input())
#
# for _ in range(N):
#     s1, s2 = map(str, input().split())
#     result = 'Possible'
#     if len(s1) != len(s2):
#         result = 'Impossible'
#     else:
#         for i in s1:
#             if i not in s2:
#                 result = 'Impossible'
#                 break
#     print(result)

