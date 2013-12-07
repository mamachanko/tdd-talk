import unittest


def my_function():
    return True


class SomeTest(unittest.TestCase):

    def test_asserts_true(self):
        self.assertTrue(my_function())

    def test_asserts_false(self):
        self.assertFalse(my_function())

    def test_asserts_equality(self):
        self.assertEqual(4, 4)

    def test_asserts_inequality(self):
        self.assertNotEqual(5, 4)

    def test_asserts_exception(self):
        with self.assertRaises(Exception):
            raise Exception()


if __name__ == '__main__':
    unittest.main(verbosity=2)
