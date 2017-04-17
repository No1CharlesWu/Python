"""

You are given an array (which will have a length of at least 3, but could be 
very large) containing integers. The array is either entirely comprised of odd 
integers or entirely comprised of even integers except for a single integer N. 
Write a method that takes the array as an argument and returns N.

For example:
[2, 4, 0, 100, 4, 11, 2602, 36]
Should return: 11
[160, 3, 1719, 19, 11, 13, -21]
Should return: 160

Sample Tests:
test.assert_equals(find_outlier([2,6,8,10,3]), 3)

"""


# Solution:
from collections import Counter


def find_outlier(integers):
    # TODO: 写完
    l = sorted(set(integers))
    print(type(l))
    c = Counter()
    guard = l[0]
    l = l[1:]
    for i, num in enumerate(l):
        tmp = (num - guard)
        print(guard, tmp)

    print(l, l[0])
    return None


print(find_outlier([12, 160, 2, 6, 8, 10, 2, 3]))
print(find_outlier([160, 3, 1719, 19, 11, 13, -21]))
