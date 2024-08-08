import unittest
from ucalcx import Measurement, Unit, MetricPrefix, Quantity
from ucalcx.length.metric import Meter
from ucalcx.length.imperial import Inch, Foot
from ucalcx.time import Second, Minute, Hour, Day

class DummyUnit(Unit):
    def __init__(self, name, symbol, metric_prefix, quantity):
        super().__init__(metric_prefix)
        self.name = name
        self.symbol = symbol
        self.quantity = quantity

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

    def test_add_operator(self):
        measurement2 = Measurement(200, self.unit1)
        result = self.measurement + measurement2
        self.assertEqual(result.value, 300)
        self.assertEqual(result.unit, self.unit1)

class TestLengthMeasurementOps(unittest.TestCase):
    def setUp(self):
        self.meter = Meter()
        self.kilometer = Meter(MetricPrefix.Kilo)
        self.inch = Inch()
        self.foot = Foot()

    def test_addition(self):
        measurement1 = Measurement(100, self.meter)
        measurement2 = Measurement(200, self.meter)
        result = measurement1 + measurement2
        self.assertEqual(result.value, 300)
        self.assertEqual(result.unit, self.meter)

    def test_add_conversion(self):
        measurement1 = Measurement(100, self.meter)
        measurement2 = Measurement(2, self.kilometer)
        result = measurement1 + measurement2
        self.assertEqual(result.value, 2100)
        self.assertEqual(result.unit, self.meter)

    def test_add_conversion_imperial(self):
        measurement1 = Measurement(100, self.meter)
        measurement2 = Measurement(2, self.foot)
        result = measurement1 + measurement2
        self.assertEqual(result.value, 100.6096)
        self.assertEqual(result.unit, self.meter)

    def test_scalar_multiplication(self):
        measurement = Measurement(100, self.meter)
        result = measurement.mul_scalar(2)
        self.assertEqual(result.value, 200)
        self.assertEqual(result.unit, self.meter)

    def test_scalar_multiplication_imperial(self):
        measurement = Measurement(100, self.foot)
        result = measurement.mul_scalar(2)
        self.assertEqual(result.value, 200)
        self.assertEqual(result.unit, self.foot)

class TestTimeMeasurementOps(unittest.TestCase):
    def setUp(self):
        self.second = Second()
        self.minute = Minute()
        self.hour = Hour()
        self.day = Day()

    def test_addition(self):
        measurement1 = Measurement(100, self.second)
        measurement2 = Measurement(200, self.second)
        result = measurement1 + measurement2
        self.assertEqual(result.value, 300)
        self.assertEqual(result.unit, self.second)

    def test_add_conversion(self):
        measurement1 = Measurement(100, self.second)
        measurement2 = Measurement(2, self.minute)
        result = measurement1 + measurement2
        self.assertEqual(result.value, 220)
        self.assertEqual(result.unit, self.second)