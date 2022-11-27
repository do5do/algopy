from sympy import Symbol, solve
a, b, c, d, e, f = map(int, input().split())

x = Symbol('x')
y = Symbol('y')
equation1 = a * x + b * y - c
equation2 = d * x + e * y - f
result = solve((equation1, equation2), dict=True) # dict값을 가진 list로 반환
print(result[0][x], result[0][y])

'''
boj에서 python의 외부 라이브러리를 사용할 수 없다고 한다. -> ModuleNotFoundError
sympy는 방정식의 해를 구하는 라이브러리
'''