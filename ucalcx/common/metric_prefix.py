from enum import Enum


class MetricPrefix(Enum):
    Yotta = {"name": "yotta", "symbol": "Y", "exponent": 24}
    Zetta = {"name": "zetta", "symbol": "Z", "exponent": 21}
    Exa = {"name": "exa", "symbol": "E", "exponent": 18}
    Peta = {"name": "peta", "symbol": "P", "exponent": 15}
    Tera = {"name": "tera", "symbol": "T", "exponent": 12}
    Giga = {"name": "giga", "symbol": "G", "exponent": 9}
    Mega = {"name": "mega", "symbol": "M", "exponent": 6}
    Kilo = {"name": "kilo", "symbol": "k", "exponent": 3}
    Hecto = {"name": "hecto", "symbol": "h", "exponent": 2}
    Deca = {"name": "deca", "symbol": "da", "exponent": 1}
    Base = {"name": "", "symbol": "", "exponent": 0}
    Deci = {"name": "deci", "symbol": "d", "exponent": -1}
    Centi = {"name": "centi", "symbol": "c", "exponent": -2}
    Milli = {"name": "milli", "symbol": "m", "exponent": -3}
    Micro = {"name": "micro", "symbol": "μ", "exponent": -6}
    Nano = {"name": "nano", "symbol": "n", "exponent": -9}
    Pico = {"name": "pico", "symbol": "p", "exponent": -12}
    Femto = {"name": "femto", "symbol": "f", "exponent": -15}
    Atto = {"name": "atto", "symbol": "a", "exponent": -18}
    Zepto = {"name": "zepto", "symbol": "z", "exponent": -21}
    Yocto = {"name": "yocto", "symbol": "y", "exponent": -24}
    
    @property
    def name(self) -> str:
        return self.value["name"]
    
    @property
    def symbol(self) -> str:
        return self.value["symbol"]
    
    @property
    def exponent(self) -> float:
        return self.value["exponent"]
    