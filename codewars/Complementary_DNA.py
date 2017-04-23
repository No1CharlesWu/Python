"""
Deoxyribonucleic acid (DNA) is a chemical found in the nucleus of cells and 
carries the "instructions" for the development and functioning of living organisms.

If you want to know more http://en.wikipedia.org/wiki/DNA

In DNA strings, symbols "A" and "T" are complements of each other, as "C" and "G". 
You have function with one side of the DNA (string, except for Haskell); you need 
to get the other complementary side. DNA strand is never empty or there is no DNA 
at all (again, except for Haskell).

DNA_strand ("ATTGC") # return "TAACG"
DNA_strand ("GTAT") # return "CATA"

Sample Tests:
Test.assert_equals(DNA_strand("AAAA"),"TTTT","String AAAA is")
Test.assert_equals(DNA_strand("ATTGC"),"TAACG","String ATTGC is")
Test.assert_equals(DNA_strand("GTAT"),"CATA","String GTAT is")

"""


# Solution:
# 个人版本
def DNA_strand(dna):
    d = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
    r = ''.join([d[c] for c in dna])
    return r


# 网络版本 translate() maketrains(from, to)把from替代成to。使用translate()进行替换
def DNA_strand_new(dna):
    return dna.translate(str.maketrans("ATCG", "TAGC"))

