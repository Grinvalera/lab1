print('Task 3')
a = int(input('Enter the length of the cube edge : '))

v = int(a ** 3)
s = int(4*(a**2))
print('The volume of the cube is ' + str(v) + ' and, the square of the cube is ' + str(s) )


print('Task 14')
m1 = float(input('Enter the mass of the first body : '))
m2 = float(input('Enter the mass of the second body : '))
r = float(input('Enter the distance between them : '))

g = 6.61 * (10**-11)
f = g * m1 * m2 / (r * r)

print('The force of attraction between the bodies is equal to ' + str(f))


print('Task 28')
x = int(input('Enter your number : '))

a = x*x*x*x
b = x*x*x
c = x*x

equation = 2*a - 3*b + 4*c - 5*x + 6
print ('2x^4 - 3x^3 + 4x^2 - 5x + 6 at ' + str(x) + ' equally ' + str(equation))


print('Task 32Д')
a = int(input('Enter your number : '))

b = a * a
c = b * b
d = c * a
e = d * d
f = e * d
h = f * b
print('The number in the second degree is equal ' + str(b))
print('The number in the fifth degree is equal ' + str(d))
print('The number in the seventeenth degree is equal to ' + str(h))


print('Task 44')
x = int(input('Enter first number : '))
y = int(input('Enter second number : '))
z = int(input('Enter third number : '))

if (x + y +z) < 1:
    if y >= x <= z:
        x = (y + z)/2
        print('Half-sum of the first number = ' + str(x))
    elif x >= y <= z:
        y = (x + z)/2
        print('Half-sum of the second number = ' + str(y))
    else:
        z = (x + y)/2
        print('Half-sum of the third number = ' + str(z))
else:
    if x < y:
        x = (y + z)/2
        print('Half-sum of the first number = ' + str(x))
    else:
        y = (x + z)/2
        print('Half-sum of the second number = ' + str(x))


