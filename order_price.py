import math
import unittest


def get_order_price(sub_total):
    return math.ceil(sub_total * 1.16 * 100)/100


class GetOrderPriceTest(unittest.TestCase):

    def test_applies_16percent_vat_for_1(self):
        order_price = get_order_price(1.00)
        self.assertEqual(1.16, order_price)

    def test_applies_16percent_vat_for_odd(self):
        order_price = get_order_price(7.57)
        self.assertEqual(8.79, order_price)

    def test_applies_16percent_vat_for_10(self):
        order_price = get_order_price(10.00)
        self.assertEqual(11.60, order_price)


if __name__ == '__main__':
    unittest.main()
