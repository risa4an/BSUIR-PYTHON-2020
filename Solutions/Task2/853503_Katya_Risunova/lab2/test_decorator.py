import unittest
from lab2.decorator import to_key


class MyTestCase(unittest.TestCase):
    def test_to_key(self):
        self.assertEqual(to_key(7), '7')

    def test_wrong(self):
        self.assertNotEqual(to_key(7), 7)



if __name__ == '__main__':
    unittest.main()
