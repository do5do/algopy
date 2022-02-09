string = input()

alph = [i for i in range(97, 123)]
result = [0] * 26

for s in string:
    result[alph.index(ord(s))] += 1

print(*result)