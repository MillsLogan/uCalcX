from enum import Enum


class Quantity(Enum):
    """ 
    Enum class for physical quantities, representing their symbol and name. Physical quantities are
    properties that can be measured, such as length, time, mass, etc. See https://en.wikipedia.org/wiki/SI_base_unit
    to learn more about the SI base units.
    
    Each quantity is associated with:
    - symbol: The symbol used to represent the quantity.
    - name: The name of the quantity.
    """
    
    Length = {'symbol': 'L'}
    """ Length (L) """
    
    Time = {'symbol': 'T'}
    """ Time (T) """
    
    Mass = {'symbol': 'M'}
    """ Mass (M) """
    
    ElectricCurrent = {'symbol': 'I'}
    """ Electric Current (I) """
    
    Temperature = {'symbol': '\u0398'}
    """ Temperature (Θ) """
    AmountOfSubstance = {'symbol': 'N'}
    """ Amount of Substance (N) """
    
    LuminousIntensity = {'symbol': 'J'}
    """ Luminous Intensity (J) """
    
    @property
    def symbol(self) -> str:
        """ Returns the symbol of the quantity. """
        return self.value['symbol']
    
    @property
    def name(self) -> str:
        """ Returns the name of the quantity. """
        return self.name