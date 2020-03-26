import unittest
from lab2.n_vector import Vector


class TestVector(unittest.TestCase):
    def test_length(self):
        self.vector = Vector([12, 5])
        self.assertEqual(self.vector.len(), 13.0)

    def test_wrong_length(self):
        self.vector = Vector([12, 5])
        self.assertNotEqual(self.vector.len(), 13.1)


if __name__ == '__main__':
    unittest.main()
