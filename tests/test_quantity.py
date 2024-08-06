import unittest
from ucalcx import Quantity, MetricPrefix

class TestQuantity(unittest.TestCase):
    def test_quantity_name(self):
        self.assertEqual(Quantity.Length.name, "Length")
        self.assertEqual(Quantity.Time.name, "Time")
        self.assertEqual(Quantity.Mass.name, "Mass")
        self.assertEqual(Quantity.Temperature.name, "Temperature")
        self.assertEqual(Quantity.ElectricCurrent.name, "Electric Current")
        self.assertEqual(Quantity.AmountOfSubstance.name, "Amount of Substance")
        self.assertEqual(Quantity.LuminousIntensity.name, "Luminous Intensity")


    def test_quantity_symbol(self):
        self.assertEqual(Quantity.Length.symbol, "L")
        self.assertEqual(Quantity.Time.symbol, "T")
        self.assertEqual(Quantity.Mass.symbol, "M")
        self.assertEqual(Quantity.Temperature.symbol, "Θ")
        self.assertEqual(Quantity.ElectricCurrent.symbol, "I")
        self.assertEqual(Quantity.AmountOfSubstance.symbol, "N")
        self.assertEqual(Quantity.LuminousIntensity.symbol, "J")
