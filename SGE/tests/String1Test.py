import unittest
from src.String1 import mix_up, donuts, both_ends, fix_start


class MyTest(unittest.TestCase):
    def testDonuts(self):
        self.assertEqual(donuts(4), 'Number of donuts: 4')
        self.assertEqual(donuts(9), 'Number of donuts: 9')
        self.assertEqual(donuts(10), 'Number of donuts: many')
        self.assertEqual(donuts(99), 'Number of donuts: many')

    def testBothEnds(self):
        self.assertEqual(both_ends('spring'), 'spng')
        self.assertEqual(both_ends('Hello'), 'Helo')
        self.assertEqual(both_ends('a'), '')
        self.assertEqual(both_ends('xyz'), 'xyyz')
  
    def testFixStart(self):
        self.assertEqual(fix_start('babble'), 'ba**le')
        self.assertEqual(fix_start('aardvark'), 'a*rdv*rk')
        self.assertEqual(fix_start('google'), 'goo*le')
        self.assertEqual(fix_start('donut'), 'donut')

    def testMixUp(self):
        self.assertEqual(mix_up('mix', 'pod'), 'pox mid')
        self.assertEqual(mix_up('dog', 'dinner'), 'dig donner')
        self.assertEqual(mix_up('gnash', 'sport'), 'spash gnort')
        self.assertEqual(mix_up('pezzy', 'firm'), 'fizzy perm')

   
        
def main():
    unittest.main()

if __name__ == "__main__":
    main()
