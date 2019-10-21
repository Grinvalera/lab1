def task16(line1, line2):
    if len(line1) > len(line2):
        c = len(line1) - len(line2)
        for _ in range(c):
            print(line1)
    elif len(line1) == len(line2):
        print('Fatal error')
    else:
        c = len(line2) - len(line1)
        for _ in range(c):
            print(line2)


def task55(line1):
    str = ''
    for c in line1:
        if c not in('0', '1', '2', '3', '4', '5', '6', '7', '8', '9'):
            str = str + c
    print(str)


def task8(line):
    if 'x' in line and 'w' in line:
        if line.index('x') > line.index('w'):
         print('first element - w')
        else:
            print('first element - x')
    else:
        print('Elements is not definted')


def task34(line):
    a = len(line)
    nev_text = ''
    for i, x in enumerate(line):
        if not i % 2 == 0:
            if x == 'a' or x == 'b':
                nev_text += 'c'
            else:
                nev_text += 'a'
        else:
            nev_text += x
    print(nev_text)


def task3(line):
     s1 = int(len(line))
     s2 = s1 - 1
     s3 = line[s2]
     print([i for i in range(len(line)) if line.startswith(s3, i)])
     return line


def task47(line):
    a = len(line)
    for i in range(1):
        for _ in range(1):
            line = line.replace('abc', '')
            line = line.replace('1234567890', '')
            print(line)
        else:
            return line


from re import *
def task22(address):
    pattern = compile('(^|\s)[-a-z0-9_.]+@([-a-z0-9]+\.)+[a-z]{2,6}(\s|$)')
    is_valid = pattern.match(address)
    if is_valid:
        print('правильный email:', is_valid.group())
    else:
        print('неверный email!')


def task29(line):
    a = line.replace('a', 'ab')
    print(a)
    return a


def task60(line1, line2):
    line3 = line1.replace(line2, '')
    print(line3)
    return line3


def task42(line1):
    a = line1.index(',') + 1
    b = line1.index(',', a)
    c = line1[a: b:]
    print(c)
    return line1




print('task3')
task3('Hello oooo iknfo')

print('task16')
task16('JavaScript', 'Pascal')

print('task29')
task29('aaaaaaaaaaaaaaaaaaaaa')

print('task42')
task42('Hello, people, word')

print('task55')
task55('a1b2c3d4')

print('task8')
task8('w12345x')

print('task22')
task22('valera.grinevich@gmail.com')

print('task34')
task34('sdjgjcvblksjbhvgiauhgrhjgjk')

print('task47')
task47('hello abc3, how are abc4 you? abc2 please return in our world abc6')

print('task60')
task60('Hello word, the weather is good', 'weather' )
















