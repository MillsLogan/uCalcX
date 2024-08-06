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
        self.assertEqual(self.fathom.meters_per_unit, 1.8288)

class TestNauticalMile(unittest.TestCase):
    def setUp(self):
        self.nautical_mile = NauticalMile()
    
    def test_nautical_mile_attributes(self):
        self.assertEqual(self.nautical_mile.name, "nautical mile")
        self.assertEqual(self.nautical_mile.symbol, "nmi")
        self.assertEqual(self.nautical_mile.meters_per_unit, 1852)
