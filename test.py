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

