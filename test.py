import unittest
from first_py_file import adding


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(1, 2)  # add assertion here

    def test_adding2(self):
        expected = 8
        actual = adding(5,3)
        self.assertEqual(actual, expected)  # add assertion here

if __name__ == '__main__':
    unittest.main()
