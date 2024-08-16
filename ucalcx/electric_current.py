from .common import FundamentalQuantityUnit, FundamentalQuantity, MetricPrefix
from abc import abstractmethod, ABC

class FundamentalCurrentUnit(FundamentalQuantityUnit, ABC):
    """ A base class for units of electric current. This class should not be instantiated directly. """
    
    def __init__(self, name: str, symbol: str):
        super().__init__(name=name, symbol=symbol, quantity=FundamentalQuantity.Current)

    def _conversion_method(self, other: "FundamentalCurrentUnit", value: float) -> float:
        if not isinstance(other, FundamentalCurrentUnit):
            raise ValueError(f"Tried to convert {self} to {other}. Expected two mass units.")
                
        return value * self.amperes_per_unit() / other.amperes_per_unit()

    @abstractmethod
    def amperes_per_unit(self) -> float:
        pass
            

class Ampere(FundamentalCurrentUnit):
    """ Represents an ampere. """
    
    def __init__(self, metric_prefix: MetricPrefix=MetricPrefix.Base):
        super().__init__(name="ampere", symbol="A")
        self.metric_prefix = metric_prefix

    def amperes_per_unit(self) -> float:
        return 10 ** self.metric_prefix.exponent

    @property
    def name(self) -> str:
        return f"{self.metric_prefix.name}{super().name}" 
    
    @property
    def symbol(self) -> str:
        return f"{self.metric_prefix.symbol}{super().symbol}"
    
    
class Abampere(FundamentalCurrentUnit):
    """ Represents an abampere. """
    
    def __init__(self):
        super().__init__(name="abampere", symbol="abA")

    def amperes_per_unit(self) -> float:
        return 10
    
class Statampere(FundamentalCurrentUnit):
    """ Represents a statampere. """
    
    def __init__(self):
        super().__init__(name="statampere", symbol="statA")

    def amperes_per_unit(self) -> float:
        return 3.33564e-10

ampere = A = Ampere()
""" Ampere (A) - 10^0 amperes """

milliampere = mA = Ampere(metric_prefix=MetricPrefix.Milli)
""" Milliampere (mA) - 10^-3 amperes """

microampere = uA = Ampere(metric_prefix=MetricPrefix.Micro)
""" Microampere (uA) - 10^-6 amperes """

nanoampere = nA = Ampere(metric_prefix=MetricPrefix.Nano)
""" Nanoampere (nA) - 10^-9 amperes """

kiloampere = kA = Ampere(metric_prefix=MetricPrefix.Kilo)
""" Kiloampere (kA) - 10^3 amperes """

abampere = abA = Abampere()
""" Abampere (abA) - 10 amperes """

statampere = statA = Statampere()
""" Statampere (statA) - 3.33564e-10 amperes """
