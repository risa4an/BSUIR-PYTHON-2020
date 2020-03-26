import unittest
import random
from lab2.merge_sort import merge_sort

class MyTestCase(unittest.TestCase):
    def test_sort(self):
        with open('testin.txt', 'w') as f:
            f.writelines('{}\n'.format(random.randint(-1000000, 1000000)) for _ in range(10000))
        merge_sort('testin.txt','testout.txt')
        outlen = 0
        with open('testout.txt') as fp:

            for line in fp:
                if line == '\n':
                    break
                else:
                    next_num = int(line)
                    if outlen > 0:
                        self.assertTrue(next_num >= prev_num)
                    outlen += 1
                    prev_num = next_num
        self.assertEqual(outlen, 10000)




if __name__ == '__main__':
    unittest.main()
