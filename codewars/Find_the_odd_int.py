"""
Given an array, find the int that appears an odd number of times.
There will always be only one integer that appears an odd number of times.

Sample Tests:
test.describe("Example")
test.assert_equals(find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]), 5)

"""

from collections import Counter
from functools import reduce
import operator


# 个人版本
def find_it(seq):
    c = Counter(seq)
    for k, v in c.items():
        if v % 2 == 1:
            return k


# 网络版本一 思路相同，写法简单
def find_it_new_1(seq):
    for i in seq:
        if seq.count(i) % 2 == 1:
            return i


# 网络版本二 reduce 超简写法，思路不同, 使用运算符异或，把相同的数据排除，剩下一个多余的。
def find_it_new_2(xs):
    return reduce(operator.xor, xs)

print(find_it_new_2([20, 1, -1, 2, -2, 3, 3, 5, 5, 1, 2, 4, 20, 4, -1, -2, 5]))

print(operator.xor(20,0))
