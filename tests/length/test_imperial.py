import unittest
from ucalcx.length.imperial import Foot, Yard, Mile, Inch, Thou, Hand
from ucalcx.length.metric import Meter

class TestFoot(unittest.TestCase):
    def setUp(self):
        self.foot = Foot()
    
    def test_foot_attributes(self):
        self.assertEqual(self.foot.name, "foot")
        self.assertEqual(self.foot.symbol, "ft")
        self.assertEqual(self.foot.inches_per_unit, 12)

    def test_foot_to_yard(self):
        self.assertEqual(self.foot.convert_to(Yard(), 3), 1)

    def test_foot_to_inch(self):
        # TODO - Use exact conversions when possible, like between foot and inch
        self.assertAlmostEqual(self.foot.convert_to(Inch(), 1), 12, places=6)

class TestYard(unittest.TestCase):
    def setUp(self):
        self.yard = Yard()
    
    def test_yard_attributes(self):
        self.assertEqual(self.yard.name, "yard")
        self.assertEqual(self.yard.symbol, "yd")
        self.assertEqual(self.yard.inches_per_unit, 36)

    def test_yard_to_foot(self):
        self.assertEqual(self.yard.convert_to(Foot(), 1), 3)

class TestMile(unittest.TestCase):
    def setUp(self):
        self.mile = Mile()
    
    def test_mile_attributes(self):
        self.assertEqual(self.mile.name, "mile")
        self.assertEqual(self.mile.symbol, "mi")
        self.assertEqual(self.mile.inches_per_unit, 63360)

class TestInch(unittest.TestCase):
    def setUp(self):
        self.inch = Inch()
    
    def test_inch_attributes(self):
        self.assertEqual(self.inch.name, "inch")
        self.assertEqual(self.inch.symbol, "in")
        self.assertEqual(self.inch.meters_per_unit, 0.0254)
        self.assertEqual(self.inch.inches_per_unit, 1)

class TestThou(unittest.TestCase):
    def setUp(self):
        self.thou = Thou()
    
    def test_thou_attributes(self):
        self.assertEqual(self.thou.name, "thou")
        self.assertEqual(self.thou.symbol, "mil")
        self.assertEqual(self.thou.inches_per_unit, 0.001)

class TestHand(unittest.TestCase):
    def setUp(self):
        self.hand = Hand()
    
    def test_hand_attributes(self):
        self.assertEqual(self.hand.name, "hand")
        self.assertEqual(self.hand.symbol, "hh")
        self.assertEqual(self.hand.inches_per_unit, 4)

    def test_hand_to_meter(self):
        self.assertAlmostEqual(self.hand.convert_to(Meter(), 1), 0.1016, places=6)
