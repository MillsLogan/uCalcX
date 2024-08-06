from enum import Enum


class Quantity(Enum):
    """
    # Quantity Enum

    Represents the physical quantities that can be measured.

    Attributes:
        name (str): The name of the quantity (e.g., "Length").
        symbol (str): The generally accepted variable symbol for the quantity (e.g., "L" for Length).

    

    Example:
        >>> Quantity.Length.name
        'Length'
        >>> Quantity.Length.symbol
        'L'
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
        return super().name