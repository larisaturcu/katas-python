import unittest
import fizzbuzz as fb

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)
    def test_fizzbuzz(self):
        self.assertEqual('Fizz',fb.fizzbuzz(3))
        self.assertEqual('Buzz', fb.fizzbuzz(5))
        self.assertEqual('Fizzbuzz', fb.fizzbuzz(15))
        self.assertEqual(4, fb.fizzbuzz(4))

if __name__ == '__main__':
    unittest.main()