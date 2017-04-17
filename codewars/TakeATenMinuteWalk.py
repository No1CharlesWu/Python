"""
You live in the city of Cartesia where all roads are laid out in a perfect grid. 
You arrived ten minutes too early to an appointment, so you decided to take 
the opportunity to go for a short walk. The city provides its citizens with a 
Walk Generating App on their phones -- everytime you press the button it 
sends you an array of one-letter strings representing directions to walk (eg. 
['n', 's', 'w', 'e']). You know it takes you one minute to traverse one city block, 
so create a function that will return true if the walk the app gives you will 
take you exactly ten minutes (you don't want to be early or late!) and will, of 
course, return you to your starting point. Return false otherwise.

Note: you will always receive a valid array containing a random 
assortment of direction letters ('n', 's', 'e', or 'w' only). It will never give 
you an empty array (that's not a walk, that's standing still!).

Sample Tests:

for i in range(2): # test as many times as you want, just change the number
    test1 = create_tests(random.randint(0,20))
    test.assert_equals(isValidWalk(test1[0]),test1[1])

"""


# Solution:
def isValidWalk(walk):
    # determine if walk is valid
    if walk.count('n') == walk.count('s') and walk.count('w') == walk.count('e') and len(walk) == 10:
        return True
    return False

"""
说明：
题设是给一个只包含'n','s','w','e' 4个方位的数组，求在十分钟能否依照数组行走方向走回到原点。

解题思路：
回到原点必须 'n' 和 's' 一样，'w' 和'e' 一样才行，而且必须行走次数为10次。
"""