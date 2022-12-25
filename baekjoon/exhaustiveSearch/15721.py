# A=인원수, T=구하고자하는 번째, answer=구호
A, T, answer = [int(input().strip()) for _ in range(3)]

bun, deggi = 0, 0 # 번, 데기 개수
round = 0 # 회차
bdList = [] # 번,데기 저장 리스트
result = 0 # 결과

while True:
    round += 1

    # 번 데기 번 데기 (각 두번씩 반복)
    for _ in range(2):
        bun += 1
        deggi += 1
        bdList.append((0, bun)) # 번
        bdList.append((1, deggi)) # 데기

    # 라운드별 반복 (번 번)
    for _ in range(round + 1):
        bun += 1
        bdList.append((0, bun))  # 번

    # 라운드별 반복 (데기 데기)
    for _ in range(round + 1):
        deggi += 1
        bdList.append((1, deggi))  # 데기

    # 해당 회차에 T번째가 있는지 확인 (번과 데기의 카운트는 같기때문에 현재 값은 bun이나 deggi 둘 중 아무거나 상관없다.)
    if bun >= T: # 현재 값이 구하고자 하는 번째보다 크거나 같으면
        # 구하고자 하는 값의 인덱스를 가져온 뒤 인원수로 나눈 나머지 값을 구한다.
        result = bdList.index((answer, T)) % A
        break

print(result)

'''
너무 어렵게 생각하지 말자. 하나씩 쪼개서 코드로 풀면 됐을거 같다.
어려웠던 부분: 사람 인덱스를 구하는 방법을 쉽게 생각하지 못했다. 
'''