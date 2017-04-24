import string


# 个人版本
def print_rangoli(size):
    l = []
    width = size * 4 - 3
    alpha = string.ascii_lowercase

    for i in range(size):
        tmp = '-'.join([alpha[size-1-i+abs(j)] for j in range(-i, i+1)])
        l.append(tmp)

    for i in range(size - 2, -1, -1):
        l.append(l[i])
    for i in range(len(l)):
        print(l[i].center(width, '-'))


# 网络简洁版本
def print_rangoli_new(num):
    alpha = string.ascii_lowercase
    l = []
    for i in range(num):
        s = "-".join(alpha[i:num])
        l.append((s[::-1]+s[1:]).center(4*n-3, "-"))
    print('\n'.join(l[:0:-1]+l))

if __name__ == '__main__':
    n = int(input())
    print_rangoli_new(n)
