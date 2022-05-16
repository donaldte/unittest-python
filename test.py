
import sys
from tkinter.ttk import Widget
import unittest 

class TestStringMethods(unittest.TestCase):
    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello dear'
        self.assertEqual(s.split(), ['hello', 'dear'])
        with self.assertRaises(TypeError):
            s.split(2)
        
class MyTestCase(unittest.TestCase):

    @unittest.skip("demonstrating skipping")
    def test_nothing(self):
        self.fail("shouldn't happen")


    @unittest.skipUnless(sys.platform.startswith("win"), "requires Windows")
    def test_windows_support(self):
        # windows specific testing code
        pass
# To test run python -m unitest -v 

if __name__ == '__main__':
    unittest.main()        