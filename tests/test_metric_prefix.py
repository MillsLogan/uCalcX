import unittest
from ucalcx import MetricPrefix

class TestMetricPrefix(unittest.TestCase):
    def test_metric_prefix_attributes(self):
        self.assertEqual(MetricPrefix.Centi.symbol, 'c')
        self.assertEqual(MetricPrefix.Centi.exponent, -2)
    
    def test_convert_to(self):
        self.assertEqual(MetricPrefix.Centi.convert_to(MetricPrefix.Milli, 1), 10)
        self.assertEqual(MetricPrefix.Milli.convert_to(MetricPrefix.Centi, 10), 1)

    def test_conversion_factor(self):
        self.assertEqual(MetricPrefix.Centi.conversion_factor, 0.01)
        self.assertEqual(MetricPrefix.Milli.conversion_factor, 0.001)
