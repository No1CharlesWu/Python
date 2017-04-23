"""
Check to see if a string has the same amount of 'x's and 'o's. The method 
must return a boolean and be case insensitive. The string can contains any char.

Examples input/output:
XO("ooxx") => true
XO("xooxx") => false
XO("ooxXm") => true
XO("zpzpzpp") => true // when no 'x' and 'o' is present should return true
XO("zzoo") => false

Sample Tests:
Test.expect(xo('xo'))
Test.expect(xo('xo0'))
Test.expect(not xo('xxxoo'))

"""


# Solution:
def xo(s):
    s = s.lower()
    return s.count('x') == s.count('o')
