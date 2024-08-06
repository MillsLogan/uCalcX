import unittest
from ucalcx.length import LengthUnit
from ucalcx import MetricPrefix, Quantity, Unit

class DummyLengthUnit(LengthUnit):
    def __init__(self, name, symbol, meters_per_unit, metric_prefix=MetricPrefix.Base):
        super().__init__(name=name, symbol=symbol, metric_prefix=metric_prefix, meters_per_unit=meters_per_unit)


class DummyTimeUnit(Unit):
    def __init__(self, name, symbol, metric_prefix=MetricPrefix.Base):
        super().__init__(name=name, symbol=symbol, metric_prefix=metric_prefix, quantity=Quantity.Time)


class TestLengthUnit(unittest.TestCase):
    def setUp(self):
        self.unit1 = DummyLengthUnit(name="meter", symbol="m", meters_per_unit=1.0)
        self.unit2 = DummyLengthUnit(name="threemeters", symbol="3m", meters_per_unit=3.0)
    
    def test_conversion(self):
        # Test conversion from unit1 to unit2
        value = 3.0
        converted_value = self.unit1.convert_to(self.unit2, value)
        self.assertEqual(converted_value, 1)
        
        # Test conversion from unit2 to unit1
        value = 1.0
        converted_value = self.unit2.convert_to(self.unit1, value)
        self.assertEqual(converted_value, 3.0)

    def test_conversion_to_time_unit(self):
        # Test conversion from 'meter' to 'second'
        unit = DummyTimeUnit(name="second", symbol="s")
        with self.assertRaises(ValueError):
            self.unit1.convert_to(unit, 1.0)

    def test_conversion_to_other_prefix(self):
        # Test conversion from 'meter' to 'kilometer'
        unit = DummyLengthUnit(name="kilometer", symbol="km", metric_prefix=MetricPrefix.Kilo, meters_per_unit=1)
        value = 1000.0
        converted_value = self.unit1.convert_to(unit, value)
        self.assertEqual(converted_value, 1.0)

        # Test conversion from 'kilometer' to 'meter'
        value = 1.0
        converted_value = unit.convert_to(self.unit1, value)
        self.assertEqual(converted_value, 1000.0)
