print(100+200)

"""name = input('enter your name:\n')
"""
name = 'world'
print(name, 'hello.\n')

a = 100
if a > 100:
    print(a)
else:
    print(-a)

print('中1文')
print(len('中文'))

a = 1
b = 3
c = a/b
d = 1 - 2/3
print(d)
print(c)
if c == d:
    print('==\n')
else:
    print('!=\n')

print('a',
      'b\n''c')

names = list([1, 2, 3, 4, 5])
names.append(6)
names = tuple(range(101))

print('start', len(names))
print('pop', len(names), names[0])
for name in names:
    print(name)


def my_abs(x):
    print('my_abs', x)

my_abs(name)
a = 1
b = 2
c = 'w'
d = 's'


def my(a, b, *sb, c, d, **e):
    print('sb', a, b, sb, c, d, e)


e = 'dsb'
f = 'zxc'
my(1, 2, e, f, c = 'a', d = d, e = e, f = f)


def move(n, a, b, c):
    if n == 1:
        print('%s --> %s' % (a, c))
        return
    move(n-1, a, c, b)
    move(1, a, b, c)
    move(n-1, b, a, c)
    pass


a = 'A'
b = 'B'
c = 'C'
move(3, a, b, c)

g = "甲乙丙丁戊己庚辛壬癸"
z = "子丑寅卯辰巳午未申酉戌亥"

result = []
for i in range(60):
    print(g[i % 10] + z[i % 12])
    result.append(g[i%10] + z[i%12])
print(result)

l = list(range(5))
list = l[5:1:-1]
Str = 'abcde'
s = Str[:-4:-1]
Str = Str[0:1].upper() + Str[1:len(Str)]
a = '1'
b = '2'
c = a + b
print(isinstance(c, str))
print(c)
print(Str)
print(l)
print(list)

print(abs(-100))


class Student(object):
    def __init__(self, name, score, privateName):
        self.name = name
        self.score = score
        self.__privateName = privateName

    def print_score(self):
        print('%s 的分数是 %s。' % (self, a.score))


a = Student('wb', 100, 'lwc')
a.exe = 1000
print(a.name, a.score, a.exe)
a.print_score()
print(a._Student__privateName)

class animal(object):
    def run(self):
        print('< This is animal run() >')

class dog(animal):
    def run(self):
        print('< This is dog run() >')

class timer(object):
    def run(self):
        print('< This is timer run() >')

def run_test(animal):
    animal.run()

class test(object):
    name = []
    def __init__(self):
        self.name.append(1)

    def print_name(self):
        print('test',self.name)

run_test(animal())
run_test(dog())
run_test(timer())

print(dir(object))

a = test()
a.print_name()
a.name = 2
a.print_name()
del(a.name)
a.print_name()


class Chain(object):

    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        sb = Chain('%s/%s' % (self._path, path))
        return sb

    def __call__(self, path):
        sba = Chain('%s/%s' % (self._path, path))
        return sba


print(Chain().status.user.timeline.list)

print(Chain().users)
a = Chain().users('michael')

print(a)

from enum import Enum, unique

@unique
class Weekday(Enum):
    Sun = 0 # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6


Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)

print(Month.Jan.value)
