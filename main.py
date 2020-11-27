from math import sin, cos, tan, pi


def task3(x, y):
    try:
        ans = (sin(x) + cos(y)) * tan(x * y) / (cos(x) - sin(y))
        return ans
    except:
        return 'Введённые данные неверного формата'


def task4(x, y):
    try:
        ans = (x + y) / (x + 1) - (x * y - 12) / (34 + x)
        return ans
    except:
        return 'Введённые данные неверного формата'


def task6(x):
    try:
        ans = x - x**3 / 3 + x**5 / 5
        return ans
    except:
        return 'Введённые данные неверного формата'


def task10(x, y):
    try:
        ans = ((x + 1) / (x - 1)) ** x + 18 * x * y * y
        return ans
    except:
        return 'Введённые данные неверного формата'


def task11(x, y):
    try:
        ans = (1 + 1/(x * x))**x - 12 * x * x * y
        return ans
    except:
        return 'Введённые данные неверного формата'


def task12(x):
    try:
        ans = (x**2 - 7 * x + 10) / (x**2 - 8 * x + 12)
        return ans
    except:
        return 'Введённые данные неверного формата'


def task13(x, y):
    try:
        ans = cos(x) / (pi - 2 * x) + 16 * x * cos(x * y) - 2
        return ans
    except:
        return 'Введённые данные неверного формата'


def task14(x, y):
    try:
        ans = 2**-x - cos(x) + sin(2 * x * y)
        return ans
    except:
        return 'Введённые данные неверного формата'


def task16(x):
    try:
        ans = abs(x**2 - x**3) - ((7 * x) / (x**3 - 15 * x))
        return ans
    except:
        return 'Введённые данные неверного формата'


def task18(x):
    try:
        ans = sin((x + 1)**0.5) - sin((x - 1)**0.5)
        return ans
    except:
        return 'Введённые данные неверного формата'


def task20(x, y):
    try:
        ans = (1 + sin((x + 1)**0.5)) / (cos(12 * y - 4))
        return ans
    except:
        return 'Введённые данные неверного формата'


def task23(x, y):
    try:
        ans = 3**x - 4 * x + (y - (abs(x))**0.5)
        return ans
    except:
        return 'Введённые данные неверного формата'


def task24(x):
    try:
        ans = x - 10 * sin(x) + abs(x**4 - x**5)
        return ans
    except:
        return 'Введённые данные неверного формата'


def task25(x, y):
    try:
        ans = x - 10**sin(x) + cos(x - y)
        return ans
    except:
        return 'Введённые данные неверного формата'


def task26(x, y):
    try:
        ans = (1 + (sin(x + y))**2) / (2 + abs(x - (2 * x) / (1 + x * x * y * y))) + x
        return ans
    except:
        return 'Введённые данные неверного формата'


def task27(a, b):
    return (a + b + (a**2 + b**2)**0.5), (0.5 * a * b)


def task28(x1, y1, x2, y2, x3, y3):
    a = ((x1 - x2)**2 + (y1 - y2)**2)**0.5
    b = ((x1 - x3)**2 + (y1 - y3)**2)**0.5
    c = ((x2 - x3)**2 + (y2 - y3)**2)**0.5
    p = (a + b + c) / 2
    return (a + b + c), (p * (p - a) * (p - b) * (p - c))**0.5


def task29(r):
    return (2 * pi * r), (pi * r * r)


def task30(number):
    number = str(number)
    return int(number[0]) + int(number[1]) + int(number[2]) + int(number[3])


def task31(x, y):
    ans1 = (x**3 + y**3) / 2
    ans2 = (abs(x) * abs(y))**0.5
    return ans1, ans2


def task32(x1, y1, x2, y2):
    return ((x1 - x2)**2 + (y1 - y2)**2)**0.5


def task33(x, y):
    return x + y, x - y, x * y, x / y


def task34(a):
    ans1 = a * a
    ans2 = a * a * 6
    ans3 = a ** 3
    return ans1, ans2, ans3


def task35(a):
    return a * 3**0.5 / 4, a * 3**0.5 / 4 * 2 / a


def task36(lenght):
    r = lenght / (2 * pi)
    return pi * r * r


def task37(r1, r2):
    return pi * r2 * r2 - pi * r1 * r1


def task38(a, b, c, r):
    return sin(a) * 2 * r, sin(b) * 2 * r, sin(c) * 2 * r
