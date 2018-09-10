import unittest
import codeCracker as cc

class TestStringMethods(unittest.TestCase):

   def test_cc(self):
        my_dict = {'t' : '!', 'o' : '"', 'i': '('}        
        self.assertEqual('!"!"',cc.decrypt(my_dict, 'toto'))
        self.assertEqual('!(!(', cc.decrypt(my_dict, 'titi'))
        self.assertEqual('???', cc.decrypt(my_dict, '123'))

if __name__ == '__main__':
    unittest.main()