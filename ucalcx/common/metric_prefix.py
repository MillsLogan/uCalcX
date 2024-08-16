from enum import Enum


class MetricPrefix(Enum):
    """ Metric Prefix Enum 
    
    Provides the name, symbol, and exponent of the metric prefix.
    
    Attributes:
        name (str): The name of the metric prefix.
        symbol (str): The symbol of the metric prefix.
        exponent (float): The exponent of the metric prefix.
    """
    
    Yotta = {"name": "yotta", "symbol": "Y", "exponent": 24}
    """ Yotta (Y) - 10^24 """
    
    Zetta = {"name": "zetta", "symbol": "Z", "exponent": 21}
    """ Zetta (Z) - 10^21 """
    
    Exa = {"name": "exa", "symbol": "E", "exponent": 18}
    """ Exa (E) - 10^18 """
    
    Peta = {"name": "peta", "symbol": "P", "exponent": 15}
    """ Peta (P) - 10^15 """
    
    Tera = {"name": "tera", "symbol": "T", "exponent": 12}
    """ Tera (T) - 10^12 """
    
    Giga = {"name": "giga", "symbol": "G", "exponent": 9}
    """ Giga (G) - 10^9 """
    
    Mega = {"name": "mega", "symbol": "M", "exponent": 6}
    """ Mega (M) - 10^6 """
    
    Kilo = {"name": "kilo", "symbol": "k", "exponent": 3}
    """ Kilo (k) - 10^3 """
    
    Hecto = {"name": "hecto", "symbol": "h", "exponent": 2}
    """ Hecto (h) - 10^2 """
    
    Deca = {"name": "deca", "symbol": "da", "exponent": 1}
    """ Deca (da) - 10^1 """
    
    Base = {"name": "", "symbol": "", "exponent": 0}
    """ Base - 10^0 default """
    
    Deci = {"name": "deci", "symbol": "d", "exponent": -1}
    """ Deci (d) - 10^-1 """
    
    Centi = {"name": "centi", "symbol": "c", "exponent": -2}
    """ Centi (c) - 10^-2 """
    
    Milli = {"name": "milli", "symbol": "m", "exponent": -3}
    """ Milli (m) - 10^-3 """
    
    Micro = {"name": "micro", "symbol": "μ", "exponent": -6}
    """ Micro (μ) - 10^-6 """
    
    Nano = {"name": "nano", "symbol": "n", "exponent": -9}
    """ Nano (n) - 10^-9 """
    
    Pico = {"name": "pico", "symbol": "p", "exponent": -12}
    """ Pico (p) - 10^-12 """
    
    Femto = {"name": "femto", "symbol": "f", "exponent": -15}
    """ Femto (f) - 10^-15 """
    
    Atto = {"name": "atto", "symbol": "a", "exponent": -18}
    """ Atto (a) - 10^-18 """
    
    Zepto = {"name": "zepto", "symbol": "z", "exponent": -21}
    """ Zepto (z) - 10^-21 """
    
    Yocto = {"name": "yocto", "symbol": "y", "exponent": -24}
    """ Yocto (y) - 10^-24 """
    
    @property
    def name(self) -> str:
        """ str: The name of the metric prefix. """
        
        return self.value["name"]
    
    @property
    def symbol(self) -> str:
        """ str: The symbol of the metric prefix. """
        
        return self.value["symbol"]
    
    @property
    def exponent(self) -> float:
        """ float: The exponent of the metric prefix. """
        
        return self.value["exponent"]
    