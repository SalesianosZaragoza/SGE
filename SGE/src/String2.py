# D. verbing
# Given a string, if its length is at least 3,
# add 'ing' to its end.
# Unless it already ends in 'ing', in which case
# add 'ly' instead.
# If the string length is less than 3, leave it unchanged.
# Return the resulting string.


def verbing(s):
    if len(s) < 3:
        return s
    elif s[-3:] == 'ing':
        return s + 'ly'
    else:
        return s + 'ing'
    pass


# E. not_bad
# Given a string, find the first appearance of the
# substring 'not' and 'bad'. If the 'bad' follows
# the 'not', replace the whole 'not'...'bad' substring
# with 'good'.
# Return the resulting string.
# So 'This dinner is not that bad!' yields:
# This dinner is good!
def not_bad(s):
    if s.find('not') < s.find('bad'):
        return s[0:(s.find('not'))] + 'good' + s[s.find('bad') + 3:]
    else:
        return s
    pass


# F. front_back
# Consider dividing a string into two halves.
# If the length is even, the front and back halves are the same length.
# If the length is odd, we'll say that the extra char goes in the front half.
# e.g. 'abcde', the front half is 'abc', the back half 'de'.
# Given 2 strings, a and b, return a string of the form
#  a-front + b-front + a-back + b-back
def front_back(a, b):
    mitad_a = len(a) / 2 + len(a) % 2
    mitad_b = len(b) / 2 + len(b) % 2

    return '' + a[0:mitad_a] + b[0:mitad_b] + a[mitad_a:] + b[mitad_b:]
    pass
