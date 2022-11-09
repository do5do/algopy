import sys
from itertools import *

n = [int(sys.stdin.readline().strip()) for _ in range(9)]

talls = list(permutations(n, 7))
for tall in talls:
    if sum(tall) == 100:
        print(*sorted(tall), sep="\n")
        break
