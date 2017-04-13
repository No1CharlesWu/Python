from functools import reduce

#利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456


def str2int(s):
    def char2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
    def fn(x,y):
        return x * 10 + y
    return reduce(fn, map(char2num, s))


def str2float(s):
    n = len(s.split('.')[1])
    s = s.replace('.', '')
    num = str2int(s)
    return num / pow(10,n)


print('str2float(\'123.456\') =', str2float('123.456'))
