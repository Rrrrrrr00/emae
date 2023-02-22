a, b, c = int(input()), int(input()), int(input())
if a == 0:
    print('Увы, это не квадратное уравнение :(')
else:
    d = b**2 - 4 * a * c
    if d < 0:
        print('Увы, корней нет :(')
    elif d == 0:
        x = (-b + d ** 0.5) / (2 * a)
        print('Корень уравнения', x)
    else:
        x1 = (-b + d**0.5) / (2 * a)
        x2 = (-b - d**0.5) / (2 * a)
        print('Корни уравнения', x1, x2)