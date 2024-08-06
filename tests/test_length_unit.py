import unittest
from ucalcx.length.metric import Meter
from ucalcx.length.imperial import Foot, Yard, Mile
from ucalcx.length.nautical import NauticalMile, Fathom, Cable
from ucalcx import MetricPrefix, Measurement


class TestMetricPrefix(unittest.TestCase):
    def test_meter_init(self):
        m = Measurement(1, Meter())
        self.assertEqual(m.value, 1)
        
    def test_meter_to_foot(self):
        m = Measurement(1, Meter())
        f = m.convert_to(Foot())
        self.assertAlmostEqual(f.value, 3.28084, 6)
        
    def test_meter_to_kilometer(self):
        m = Measurement(1000, Meter())
        km = m.convert_to(Meter(MetricPrefix.Kilo))
        self.assertEqual(km.value, 1)
        
    def test_kilo_foot_to_meter(self):
        km = Measurement(1, Meter(MetricPrefix.Kilo))
        m = km.convert_to(Meter())
        self.assertEqual(m.value, 1000)
        
    def test_feet_to_yard(self):
        f = Measurement(3, Foot())
        y = f.convert_to(Yard())
        self.assertAlmostEqual(y.value, 1, 6)

    def test_mega_meter_to_mile(self):
        mm = Measurement(1, Meter(MetricPrefix.Mega))
        mile = mm.convert_to(Mile())
        self.assertAlmostEqual(mile.value, 621.37119224, 6)
        
    def test_nautical_mile_to_meter(self):
        nm = Measurement(1, NauticalMile())
        m = nm.convert_to(Meter())
        self.assertEqual(m.value, 1852)
        
    def test_fathom_to_meter(self):
        f = Measurement(1, Fathom())
        m = f.convert_to(Meter())
        self.assertAlmostEqual(m.value, 1.8288, 6)
        
    def test_cable_to_meter(self):
        c = Measurement(1, Cable())
        m = c.convert_to(Meter())
        self.assertEqual(m.value, 185.2)
        

if __name__ == '__main__':
    unittest.main()