from enum import Enum


class MetricPrefix(Enum):
    """
    Enum class for metric prefixes, representing their symbol and exponent value.

    Each metric prefix is associated with:
    - symbol: The symbol used to represent the prefix.
    - exponent: The exponent value of 10 that the prefix represents. For example, the prefix 
        'kilo' has an exponent value of 3, so 1 kilometer is equal to 1000 meters.
    """

    Yotta = {'symbol': 'Y', 'exponent': 24}
    """ Yotta (Y): Exponent value 24 """
    
    Zetta = {'symbol': 'Z', 'exponent': 21}
    """ Zetta (Z): Exponent value 21 """
    
    Exa = {'symbol': 'E', 'exponent': 18}
    """ Exa (E): Exponent value 18 """
    
    Peta = {'symbol': 'P', 'exponent': 15}
    """ Peta (P): Exponent value 15 """
    
    Tera = {'symbol': 'T', 'exponent': 12}
    """ Tera (T): Exponent value 12 """
    
    Giga = {'symbol': 'G', 'exponent': 9}
    """ Giga (G): Exponent value 9 """
    
    Mega = {'symbol': 'M', 'exponent': 6}
    """ Mega (M): Exponent value 6 """
    
    Kilo = {'symbol': 'k', 'exponent': 3}
    """ Kilo (k): Exponent value 3 """
    
    Hecto = {'symbol': 'h', 'exponent': 2}
    """ Hecto (h): Exponent value 2 """
    
    Deca = {'symbol': 'da', 'exponent': 1}
    """ Deca (da): Exponent value 1 """
    
    Base = {'symbol': '', 'exponent': 0}
    """ Base: Exponent value 0 """
    
    Deci = {'symbol': 'd', 'exponent': -1}
    """ Deci (d): Exponent value -1 """
    
    Centi = {'symbol': 'c', 'exponent': -2}
    """ Centi (c): Exponent value -2 """
    
    Milli = {'symbol': 'm', 'exponent': -3}
    """ Milli (m): Exponent value -3 """
    
    Micro = {'symbol': 'μ', 'exponent': -6}
    """ Micro (μ): Exponent value -6 """
    
    Nano = {'symbol': 'n', 'exponent': -9}
    """ Nano (n): Exponent value -9 """
    
    Pico = {'symbol': 'p', 'exponent': -12}
    """ Pico (p): Exponent value -12 """
    
    Femto = {'symbol': 'f', 'exponent': -15}
    """ Femto (f): Exponent value -15 """
    
    Atto = {'symbol': 'a', 'exponent': -18}
    """ Atto (a): Exponent value -18 """
    
    Zepto = {'symbol': 'z', 'exponent': -21}
    """ Zepto (z): Exponent value -21 """
    
    Yocto = {'symbol': 'y', 'exponent': -24}
    """ Yocto (y): Exponent value -24 """

    @property
    def symbol(self) -> str:
        """ Returns the symbol of the metric prefix. """
        return self.value['symbol']
    
    @property
    def exponent(self) -> int:
        """ Returns the exponent value of the metric prefix. """
        return self.value['exponent']
    
    @property
    def conversion_factor(self) -> float:
        """ Returns the conversion factor of the metric prefix. """
        return 10 ** self.exponent
    
    @property
    def name(self) -> str:
        """ Returns the name of the metric prefix. """
        return self.name

    def convert_to(self, other: 'MetricPrefix', value: float) -> float:
        """ 
        Converts a value from this metric prefix to another metric prefix. 
        
        Args:
        - other: The metric prefix to convert the value to.
        - value: The value to convert.
        
        Returns:
        - The converted value.
        
        Example:
        >>> MetricPrefix.Kilo.convert_to(MetricPrefix.Mega, 1)
        0.001
        >>> MetricPrefix.Kilo.convert_to(MetricPrefix.Base, 1)
        1000
        """
        
        return value * 10 ** (self.exponent - other.exponent)