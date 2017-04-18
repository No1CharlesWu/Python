"""

Write a function

triple_double(num1, num2)
which takes in numbers num1 and num2 and returns 1 if there is a 
straight triple of a number at any place in num1 and also a straight 
double of the same number in num2.

For example:
triple_double(451999277, 41177722899) == 1 // num1 has straight triple 999s and 
                                          // num2 has straight double 99s
triple_double(1222345, 12345) == 0 // num1 has straight triple 2s but num2 has only a single 2
triple_double(12345, 12345) == 0
triple_double(666789, 12345667) == 1

If this isn't the case, return 0

Sample Tests:

test.assert_equals(triple_double(451999277, 41177722899), 1)
test.assert_equals(triple_double(1222345, 12345), 0)
test.assert_equals(triple_double(12345, 12345), 0)
test.assert_equals(triple_double(666789, 12345667), 1)
test.assert_equals(triple_double(10560002, 100), 1)

"""


# Solution:
# 个人版本
def devision(string, num):
    set_str = set([])
    for i in range(len(string) - num + 1):
        set_str.add(string[i:i+num])
    return set_str


def create_set(num):
    set_num = set([])
    for i in '1234567890':
        set_num.add(i * num)
    return set_num


def triple_double(num1, num2):
    str1 = str(num1)
    str2 = str(num2)
    c1 = devision(str1, 3) & create_set(3)
    c2 = devision(str2, 2) & create_set(2)
    l = []
    for i in c1:
        for j in c2:
            if i[0] == j[0]:
                return 1
    return 0


# 网络版本一
def triple_double_1(num1, num2):
    for x in range(10):
        if str(x) * 3 in str(num1):
            if str(x) * 2 in str(num2):
                return 1
    return 0


# 网络版本二
def triple_double_2(num1, num2):
    return any([i * 3 in str(num1) and i * 2 in str(num2) for i in '0123456789'])


# 个人修改版本
def triple_double_repire(num1, num2):
    for i in str(range(10)):
        if i * 3 in str(num1) and i * 2 in str(num2):
            return 1
    return 0

"""
学习说明：
if i * 3 in str(num1):
如果 str(num1) 中包含 i * 3 这个字符串，就如何如何。。可以从字符串中查询对应的子串。

any( list() )
如果 any() 中非空，返回 True 空返回 False  
"""

print(triple_double(1222233345, 2342))
print(triple_double(666789, 12345667))

print(any([]))
print(any([None, {1: None}, '']))

