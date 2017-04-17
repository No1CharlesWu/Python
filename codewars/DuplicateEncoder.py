"""
The goal of this exercise is to convert a string to a new string where each 
character in the new string is '(' if that character appears only once in the 
original string, or ')' if that character appears more than once in the original 
string. Ignore capitalization when determining if a character is a duplicate.

Examples:
"din" => "((("
"recede" => "()()()"
"Success" => ")())())"
"(( @" => "))(("

Sample Tests:
Test.assert_equals(duplicate_encode("din"),"(((")
Test.assert_equals(duplicate_encode("recede"),"()()()")
Test.assert_equals(duplicate_encode("Success"),")())())","should ignore case")
Test.assert_equals(duplicate_encode("(( @"),"))((")

"""

from collections import Counter


# Solution:
# 这是我写的版本
def duplicate_encode(word):
    word = word.lower()
    c_dict = Counter()
    for ch in word:
        c_dict[ch] = c_dict[ch] + 1
    re_str = ''
    for ch in word:
        if c_dict[ch] > 1:
            re_str += ')'
        else:
            re_str += '('
    return re_str


# c_dict = Counter(word) 可以直接计算word中各个字符的数量
# 用join拼接字符串，用列表生成式生成各个字符
# 不过我并不喜欢带太多判断的列表生成式，因为这会让我看的不清楚
def duplicate_encode_new(word):
    word = word.lower()

    c_dict = Counter(word)

    re_str = ''.join(('(' if c_dict[ch] == 1 else ')') for ch in word)

    return re_str

duplicate_encode_new("Success")
duplicate_encode("din")
duplicate_encode("(( @")
