import unittest
import logic

import unittest

def square(x):
    return x * x

class TestSquare(unittest.TestCase):

    def test_positives(self):
        self.assertEqual(square(3), 9)
        self.assertEqual(square(5), 25)

    def test_negatives(self):
        self.assertEqual(square(-2), 4)

if __name__ == '__main__':
    unittest.main()



if __name__ == '__main__':
    unittest.main()