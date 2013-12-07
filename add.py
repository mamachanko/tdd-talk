import unittest


def add(x, y):
    for z in range(y):
        x = x + 1
    return x


class AddTest(unittest.TestCase):

    def test_returns_1_plus_1(self):
        result = add(1, 1)
        self.assertEqual(2, result)

    def test_returns_0_plus_8(self):
        result = add(0, 8)
        self.assertEqual(8, result)

    def test_returns_minus_10_plus_1(self):
        result = add(-10, 1)
        self.assertEqual(-9, result)

    def test_returns_1_plus_minus_10(self):
        result = add(1, -10)
        self.assertEqual(-9, result)


if __name__ == '__main__':
    unittest.main()
