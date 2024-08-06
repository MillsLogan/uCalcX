import unittest
from ucalcx import Measurement, Unit, MetricPrefix, Quantity

class DummyUnit(Unit):
    def __init__(self, name, symbol, metric_prefix, quantity):
        super().__init__(name, symbol, metric_prefix, quantity)

    def convert_to(self, other, value):
        return value * 10**(self.metric_prefix.exponent - other.metric_prefix.exponent)

class TestMeasurement(unittest.TestCase):
    def setUp(self):
        self.unit1 = DummyUnit("unit1", "u1", MetricPrefix.Base, Quantity.Length)
        self.unit2 = DummyUnit("unit2", "u2", MetricPrefix.Kilo, Quantity.Length)
        self.measurement = Measurement(100, self.unit1)
    
    def test_conversion(self):
        converted_measurement = self.measurement.convert_to(self.unit2)
        self.assertEqual(converted_measurement.value, 0.1)
        self.assertEqual(converted_measurement.unit, self.unit2)

    def test_conversion_different_quantity(self):
        unit3 = DummyUnit("unit3", "u3", MetricPrefix.Base, Quantity.Time)
        with self.assertRaises(ValueError):
            self.measurement.convert_to(unit3)

    def test_string_repersentation(self):
        self.assertEqual(str(self.measurement), "100 u1")
        self.assertEqual(str(self.measurement.convert_to(self.unit2)), "0.1 ku2")

if __name__ == '__main__':
    unittest.main()