# A. match_ends
# Given a list of strings, return the count of the number of
# strings where the string length is 2 or more and the first
# and last chars of the string are the same.
# Note: python does not have a ++ operator, but += works.


def match_ends(words):
    count = 0
    for word in words:
        if (len(word) > 1) and (word[0] == word[len(word) - 1]):
            count += 1
    return count
    pass


# B. front_x
# Given a list of strings, return a list with the strings
# in sorted order, except group all the strings that begin with 'x' first.
# e.g. ['mix', 'xyz', 'apple', 'xanadu', 'aardvark'] yields
# ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']
# Hint: this can be done by making 2 lists and sorting each of them
# before combining them.


def front_x(words):
    list1 = []
    list2 = []

    for word in words:
        if word[0] == 'x':
            list1.append(word)
        else:
            list2.append(word)
    list1.sort()
    list2.sort()
    return list1 + list2
    pass


# C. sort_last
# Given a list of non-empty tuples, return a list sorted in increasing
# order by the last element in each tuple.
# e.g. [(1, 7), (1, 3), (3, 4, 5), (2, 2)] yields
# [(2, 2), (1, 3), (3, 4, 5), (1, 7)]
# Hint: use a custom key= function to extract the last element form each tuple.


def my_function(tuple):
    return tuple[len(tuple) - 1]


def sort_last(tuples):
    return sorted(tuples, key=my_function)
