import unittest
from src.String2 import verbing, not_bad, front_back


class MyTest(unittest.TestCase):
    def testVerbing(self):
        self.assertEqual(verbing('hail'), 'hailing')
        self.assertEqual(verbing('swiming'), 'swimingly')
        self.assertEqual(verbing('do'), 'do')
        
    def testNotBad(self):
        self.assertEqual(not_bad('This movie is not so bad'), 'This movie is good')
        self.assertEqual(not_bad('This dinner is not that bad!'), 'This dinner is good!')
        self.assertEqual(not_bad('This tea is not hot'), 'This tea is not hot')
        self.assertEqual(not_bad("It's bad yet not"), "It's bad yet not")
        
    def testFrontBack(self):
        self.assertEqual(front_back('abcd', 'xy'), 'abxcdy')
        self.assertEqual(front_back('abcde', 'xyz'), 'abcxydez')
        self.assertEqual(front_back('Kitten', 'Donut'), 'KitDontenut')
    
   
        
def main():
    unittest.main()

if __name__ == "__main__":
    main()
