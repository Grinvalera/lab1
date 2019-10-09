def task3(a = 1):
    v = int(a ** 3)
    s = int(4 * (a ** 2))
    print('The volume of the cube is ' + str(v) + ' and, the square of the cube is ' + str(s))
def task14(m1 = 1, m2 = 2, r = 3):
    import math
    g = 6.61 * (10 ** -11)
    f = g * m1 * m2 / (r * r)
    print('The force of attraction between the bodies is equal to ' + str(f))
def task28(x = 1):
    a = x * x * x * x
    b = x * x * x
    c = x * x
    equation = 2 * a - 3 * b + 4 * c - 5 * x + 6
    print('2x^4 - 3x^3 + 4x^2 - 5x + 6 at ' + str(x) + ' equally ' + str(equation))
def task32d(a = 1):
    b = a * a
    c = b * b
    d = c * a
    e = d * d
    f = e * d
    h = f * b
    print('The number in the second degree is equal ' + str(b))
    print('The number in the fifth degree is equal ' + str(d))
    print('The number in the seventeenth degree is equal to ' + str(h))
def task44(x = 1, y = 1, z = 1):
    if (x + y + z) < 1:
        if y >= x <= z:
            x = (y + z) / 2
            print('Half-sum of the first number = ' + str(x))
        elif x >= y <= z:
            y = (x + z) / 2
            print('Half-sum of the second number = ' + str(y))
        else:
            z = (x + y) / 2
            print('Half-sum of the third number = ' + str(z))
    else:
        if x < y:
            x = (y + z) / 2
            print('Half-sum of the first number = ' + str(x))
        else:
            y = (x + z) / 2
            print('Half-sum of the second number = ' + str(x))


task3()
task14()
task28()
task32d()
task44()