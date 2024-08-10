from enum import Enum


class FundamentalQuantity(Enum):
    Length = {"name": "Length", "symbol": "L"}
    Mass = {"name": "Mass", "symbol": "M"}
    Time = {"name": "Time", "symbol": "T"}
    Current = {"name": "Current", "symbol": "I"}
    Temperature = {"name": "Temperature", "symbol": "T"}
    AmountOfSubstance = {"name": "Amount of Substance", "symbol": "N"}
    LuminousIntensity = {"name": "Luminous Intensity", "symbol": "J"}
    Unitless = {"name": "Coefficient", "symbol": ""}
    
    @property
    def quantity_name(self):
        return self.value["name"]

    @property
    def quantity_symbol(self):
        return self.value["symbol"]
    
    