import unittest
from ucalcx import Unit, MetricPrefix, Quantity


class TestUnit(unittest.TestCase):
    def setUp(self):
        self.meter = Unit("meter", "m", MetricPrefix.Base, Quantity.Length)
        self.kilometer = Unit("meter", "m", MetricPrefix.Kilo, Quantity.Length)
        self.yoctometer = Unit("meter", "m", MetricPrefix.Yocto, Quantity.Length)

    def test_full_name(self):
        self.assertEqual(self.meter.full_name, "meter")
        self.assertEqual(self.kilometer.full_name, "kilometer")
        self.assertEqual(self.yoctometer.full_name, "yoctometer")

    def test_full_symbol(self):
        self.assertEqual(self.meter.full_symbol, "m")
        self.assertEqual(self.kilometer.full_symbol, "km")
        self.assertEqual(self.yoctometer.full_symbol, "ym")

if __name__ == '__main__':
    unittest.main()