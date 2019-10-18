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


'''def task47(line = "hello abc3, how are abc4 you? abc please return in our world abc6"):
    b = 'abc'
    for char in b:
        a = line.replace(char, "")
        print(a)'''
















#task47()

task3('Hello oooo iknfo')

task34('sdjgjcvblksjbhvgiauhgrhjgjk')

task8('w12345x')

task55('a1b2c3d4')

task16('JavaScript', 'Pascal')
