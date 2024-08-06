import unittest
from ucalcx.length.metric import Meter
from ucalcx import MetricPrefix

class TestMeter(unittest.TestCase):
    def setUp(self):
        self.meter = Meter()
    
    def test_meter_attributes(self):
        self.assertEqual(self.meter.name, "meter")
        self.assertEqual(self.meter.symbol, "m")
        self.assertEqual(self.meter.conversion_factor, 1)

    def test_conversion(self):
        value = 1
        converted_value = self.meter.convert_to(self.meter, value)  # Should remain 1
        self.assertEqual(converted_value, 1)

    def test_conversion_to_other_prefix(self):
        kilometer = Meter(MetricPrefix.Kilo)
        value = 1000.0
        converted_value = self.meter.convert_to(kilometer, value)
        self.assertEqual(converted_value, 1.0)

        value = 1.0
        converted_value = kilometer.convert_to(self.meter, value)
        self.assertEqual(converted_value, 1000.0)

    def test_representation(self):
        self.assertEqual(str(self.meter), "meter (m)")

if __name__ == '__main__':
    unittest.main()
