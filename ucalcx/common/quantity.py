from enum import Enum


class FundamentalQuantity(Enum):
    """ Fundamental Quantity Enum
    
    Provides the name and symbol of the fundamental quantity.
    
    Attributes:
        name (str): The name of the fundamental quantity.
        symbol (str): The symbol of the fundamental quantity.
    """
    
    Length = {"name": "Length", "symbol": "L"}
    """ Length (L) """
    
    Mass = {"name": "Mass", "symbol": "M"}
    """ Mass (M) """
    
    Time = {"name": "Time", "symbol": "T"}
    """ Time (T) """
    
    Current = {"name": "Current", "symbol": "I"}
    """ Current (I) """
    
    Temperature = {"name": "Temperature", "symbol": "T"}
    """ Temperature (T) """
    
    AmountOfSubstance = {"name": "Amount of Substance", "symbol": "N"}
    """ Amount of Substance (N) """
    
    LuminousIntensity = {"name": "Luminous Intensity", "symbol": "J"}
    """ Luminous Intensity (J) """
    
    Unitless = {"name": "Coefficient", "symbol": ""}
    """ Unitless (1) """
    
    @property
    def quantity_name(self):
        """ Returns the name of the fundamental quantity. """
        
        return self.value["name"]

    @property
    def quantity_symbol(self):
        """ Returns the symbol of the fundamental quantity. """
        
        return self.value["symbol"]
    
    