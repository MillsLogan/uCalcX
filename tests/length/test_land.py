import unittest
from ucalcx.length.land import Rod, Chain, Furlong

class TestRod(unittest.TestCase):
    def setUp(self):
        self.rod = Rod()
    
    def test_rod_attributes(self):
        self.assertEqual(self.rod.name, "rod")
        self.assertEqual(self.rod.symbol, "rd")
        self.assertEqual(self.rod.inches_per_unit, 198.0)

class TestChain(unittest.TestCase):
    def setUp(self):
        self.chain = Chain()
    
    def test_chain_attributes(self):
        self.assertEqual(self.chain.name, "chain")
        self.assertEqual(self.chain.symbol, "ch")
        self.assertEqual(self.chain.inches_per_unit, 792.0)

class TestFurlong(unittest.TestCase):
    def setUp(self):
        self.furlong = Furlong()
    
    def test_furlong_attributes(self):
        self.assertEqual(self.furlong.name, "furlong")
        self.assertEqual(self.furlong.symbol, "fur")
        self.assertEqual(self.furlong.inches_per_unit, 7920.0)

