sides = [3, 2, 4, 7, 5, 12, 11, 13, 15, 16, 14, 14]
sides = sorted(sides, reverse=True)
smax = 0
for i1 in range(len(sides) - 2):
    for i2 in range(i1 + 1, len(sides) - 1):
        for i3 in range(i2 + 1, len(sides)):
            a = sides[i1]
            b = sides[i2]
            c = sides[i3]
            if a + b > c and a + c > b and b + c > a:
                p = (a + b + c) / 2
                s = (p * (p - a) * (p - b) * (p - c))**0.5
                smax = max(s, smax)
print('Максимальная площадь треугольника', smax)
