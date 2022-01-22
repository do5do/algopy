cards = [i for i in range(1, 21)]
section = []
for _ in range(10):
    section.append(tuple(map(int, input().split())))

for i in section:
    cards[i[0]-1:i[1]] = list(reversed(cards[i[0]-1:i[1]]))

print(*cards)