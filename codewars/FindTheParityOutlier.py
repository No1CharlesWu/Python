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
def find_outlier(integers):
    c_odd = []
    c_even = []
    for i in integers:
        if i % 2 == 0:
            c_even.append(i)
        else:
            c_odd.append(i)

    return c_even[0] if len(c_even) == 1 else c_odd[0]


print(find_outlier([12, 160, 2, 6, 8, 10, 2, 3]))
print(find_outlier([160, 3, 1719, 19, 11, 13, -21]))
