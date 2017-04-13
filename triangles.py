# 期待输出:
# [1]
# [1, 1]
# [1, 2, 1]
# [1, 3, 3, 1]
# [1, 4, 6, 4, 1]
# [1, 5, 10, 10, 5, 1]
# [1, 6, 15, 20, 15, 6, 1]
# [1, 7, 21, 35, 35, 21, 7, 1]
# [1, 8, 28, 56, 70, 56, 28, 8, 1]
# [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
# -*- coding: utf-8 -*-


def my_triangles():
    """
    #个人编写杨辉三角
    :return: none
    """
    count = 1
    l = []
    while True:
        if count == 1:
            l = [0, 1, 0]
            yield l[1:len(l)-1]
        else:
            y = []
            for i, num in enumerate(l):
                y.append(num + l[i-1])
            y.append(0)
            l = y
            yield l[1:len(l)-1]
        count = count + 1


def triangles():
    """
    #网上比较简洁的写法使用列表生成器
    :return: none
    """
    l = [1]
    while True:
        yield l
        l = [1] + [l[i] + l[i-1] for i in range(len(l)) if i > 0] + [1]


n = 0
for t in triangles():
    print(t)
    n = n + 1
    if n == 10:
        break
