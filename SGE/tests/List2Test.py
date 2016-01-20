import unittest
from src.Christmas import FunWithSnow
from src.List2 import remove_adjacent, linear_merge

clase = FunWithSnow()

class MyTest(unittest.TestCase):
    def testRemoveAdjacement(self):
        self.assertTrue(remove_adjacent([1, 2, 2, 3]), [1, 2, 3])
        self.assertTrue(remove_adjacent([2, 2, 3, 3, 3]), [2, 3])
        self.assertTrue(remove_adjacent([]), [])

    def testLinearMerge(self):
        self.assertTrue(linear_merge(['aa', 'xx', 'zz'], ['bb', 'cc']),
                         ['aa', 'bb', 'cc', 'xx', 'zz'])
        self.assertTrue(linear_merge(['aa', 'xx'], ['bb', 'cc', 'zz']),
       ['aa', 'bb', 'cc', 'xx', 'zz'])
        self.assertTrue(linear_merge(['aa', 'aa'], ['aa', 'bb', 'bb']),
       ['aa', 'aa', 'aa', 'bb', 'bb'])

    
        
def main():
    unittest.main()

if __name__ == "__main__":
    main()