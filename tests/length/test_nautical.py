import unittest
from ucalcx.length.nautical import NauticalMile, Fathom, Cable

class TestCable(unittest.TestCase):
    def setUp(self):
        self.rod = Cable()
    
    def test_rod_attributes(self):
        self.assertEqual(self.rod.name, "cable")
        self.assertEqual(self.rod.symbol, "cbl")
        self.assertEqual(self.rod.meters_per_unit, 185.2)

class TestFathom(unittest.TestCase):
    def setUp(self):
        self.fathom = Fathom()
    
    def test_fathom_attributes(self):
        self.assertEqual(self.fathom.name, "fathom")
        self.assertEqual(self.fathom.symbol, "ftm")
        self.assertEqual(self.fathom.inches_per_unit, 72.0)

class TestNauticalMile(unittest.TestCase):
    def setUp(self):
        self.nautical_mile = NauticalMile()
    
    def test_nautical_mile_attributes(self):
        self.assertEqual(self.nautical_mile.name, "nautical_mile")
        self.assertEqual(self.nautical_mile.symbol, "NM")
        self.assertEqual(self.nautical_mile.meters_per_unit, 1852)
