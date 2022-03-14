n = int(input())

for _ in range(n):
    left = []
    right = []
    string = list(map(str, input()))
    for s in string:
        if s == "<":
            if left:
                right.append(left.pop())
        elif s == ">":
            if right:
                left.append(right.pop())
        elif s == "-":
            if left:
                left.pop()
        else:
            left.append(s)
    left.extend(reversed(right))
    print("".join(left))