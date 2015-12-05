import unittest
from src.List1 import match_ends, front_x, sort_last

class MyTest(unittest.TestCase):
    
    def testMatchEnds(self):
        self.assertEqual(match_ends(['aba', 'xyz', 'aa', 'x', 'bbb']), 3)
        self.assertEqual(match_ends(['', 'x', 'xy', 'xyx', 'xx']), 2)
        self.assertEqual(match_ends(['aaa', 'be', 'abc', 'hello']), 1)

    def testFront(self):
        self.assertEqual(front_x(['bbb', 'ccc', 'axx', 'xzz', 'xaa']),
                         ['xaa', 'xzz', 'axx', 'bbb', 'ccc'])
        self.assertEqual(front_x(['ccc', 'bbb', 'aaa', 'xcc', 'xaa']),
                         ['xaa', 'xcc', 'aaa', 'bbb', 'ccc'])
        self.assertEqual(front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark']),
                         ['xanadu', 'xyz', 'aardvark', 'apple', 'mix'])

        
    def testSortLast(self):
        self.assertEqual(sort_last([(1, 3), (3, 2), (2, 1)]),
                         [(2, 1), (3, 2), (1, 3)])
        self.assertEqual(sort_last([(2, 3), (1, 2), (3, 1)]),
                         [(3, 1), (1, 2), (2, 3)])
        self.assertEqual(sort_last([(1, 7), (1, 3), (3, 4, 5), (2, 2)]),
                         [(2, 2), (1, 3), (3, 4, 5), (1, 7)])
        
def main():
    unittest.main()

if __name__ == "__main__":
    main()
