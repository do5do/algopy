st = list(input().strip())
n = int(input())

cursor = len(st)
for _ in range(n):
    line = input()
    if line[0] == 'L':
        if cursor != 0:
            cursor -= 1
    elif line[0] == 'D':
        if cursor != len(st):
            cursor += 1
    elif line[0] == 'B':
        if cursor != 0:
            del st[cursor-1] # index로 삭제, remove()는 값으로 삭제하는 함수 / O(N)
            cursor -= 1
    elif line[0] == 'P':
        st.insert(cursor, line[2]) # O(N)
        cursor += 1

print("".join(st))
# 리스트에서 가운데 원소를 삭제하거나 추가하는 것은 해당 지점부터 뒤로 한칸씩 미는 거기때문에 시간복잡도가 O(N)이다.
# => 시간초과