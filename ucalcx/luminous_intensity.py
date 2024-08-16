from .common import FundamentalQuantityUnit, FundamentalQuantity, MetricPrefix
from abc import abstractmethod, ABC

class FundamentalLuminousUnit(FundamentalQuantityUnit, ABC):
    """ A base class for units of luminous intensity. This class should not be instantiated directly. """
    
    def __init__(self, name: str, symbol: str):
        super().__init__(name=name, symbol=symbol, quantity=FundamentalQuantity.Current)

    def _conversion_method(self, other: "FundamentalLuminousUnit", value: float) -> float:
        if not isinstance(other, FundamentalLuminousUnit):
            raise ValueError(f"Tried to convert {self} to {other}. Expected two amount of substance units.")
                
        return value * self.candela_per_unit() / other.candela_per_unit()

    @abstractmethod
    def candela_per_unit(self) -> float:
        pass
            

class Candela(FundamentalLuminousUnit):
    """ Represents a candela. """
    
    def __init__(self, metric_prefix: MetricPrefix=MetricPrefix.Base):
        super().__init__(name="candela", symbol="cd")
        self.metric_prefix = metric_prefix

    def candela_per_unit(self) -> float:
        return 10 ** self.metric_prefix.exponent
    
    @property
    def name(self) -> str:
        return f"{self.metric_prefix.name}{super().name}"
    
    @property
    def symbol(self) -> str:
        return f"{self.metric_prefix.symbol}{super().symbol}"
    
candela = cd = Candela()
""" Candela (cd) - 10^0 candelas """

millicandela = mcd = Candela(metric_prefix=MetricPrefix.Milli)
""" Millicandela (mcd) - 10^-3 candelas """

microcandela = ucd = Candela(metric_prefix=MetricPrefix.Micro)
""" Microcandela (ucd) - 10^-6 candelas """

nanocandela = ncd = Candela(metric_prefix=MetricPrefix.Nano)
""" Nanocandela (ncd) - 10^-9 candelas """

kilocandela = kcd = Candela(metric_prefix=MetricPrefix.Kilo)
""" Kilocandela (kcd) - 10^3 candelas """
    

