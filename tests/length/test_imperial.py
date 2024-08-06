import unittest
from ucalcx.length.imperial import Foot, Yard, Mile, Inch, Thou, Hand

class TestFoot(unittest.TestCase):
    def setUp(self):
        self.foot = Foot()
    
    def test_foot_attributes(self):
        self.assertEqual(self.foot.name, "foot")
        self.assertEqual(self.foot.symbol, "ft")
        self.assertEqual(self.foot.conversion_factor, 0.3048)

class TestYard(unittest.TestCase):
    def setUp(self):
        self.yard = Yard()
    
    def test_yard_attributes(self):
        self.assertEqual(self.yard.name, "yard")
        self.assertEqual(self.yard.symbol, "yd")
        self.assertEqual(self.yard.conversion_factor, 0.9144)

class TestMile(unittest.TestCase):
    def setUp(self):
        self.mile = Mile()
    
    def test_mile_attributes(self):
        self.assertEqual(self.mile.name, "mile")
        self.assertEqual(self.mile.symbol, "mi")
        self.assertEqual(self.mile.conversion_factor, 1609.344)

class TestInch(unittest.TestCase):
    def setUp(self):
        self.inch = Inch()
    
    def test_inch_attributes(self):
        self.assertEqual(self.inch.name, "inch")
        self.assertEqual(self.inch.symbol, "in")
        self.assertEqual(self.inch.conversion_factor, 0.0254)

class TestThou(unittest.TestCase):
    def setUp(self):
        self.thou = Thou()
    
    def test_thou_attributes(self):
        self.assertEqual(self.thou.name, "thou")
        self.assertEqual(self.thou.symbol, "mil")
        self.assertEqual(self.thou.conversion_factor, 0.0000254)

class TestHand(unittest.TestCase):
    def setUp(self):
        self.hand = Hand()
    
    def test_hand_attributes(self):
        self.assertEqual(self.hand.name, "hand")
        self.assertEqual(self.hand.symbol, "h")
        self.assertEqual(self.hand.conversion_factor, 0.1016)
