from common import FundamentalQuantityUnit, FundamentalQuantity, MetricPrefix
from abc import abstractmethod, ABC

class FundamentalCurrentUnit(FundamentalQuantityUnit, ABC):
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
    def __init__(self, metric_prefix: MetricPrefix=MetricPrefix.Base):
        super().__init__(name="ampere", symbol="A")
        self.metric_prefix = metric_prefix

    def grams_per_unit(self) -> float:
        return 10 ** self.metric_prefix.exponent

    @property
    def name(self) -> str:
        return f"{self.metric_prefix.name}{super().name}" 
    
    @property
    def symbol(self) -> str:
        return f"{self.metric_prefix.symbol}{super().symbol}"
    

ampere = A = Ampere()
milliampere = mA = Ampere(metric_prefix=MetricPrefix.Milli)
microampere = uA = Ampere(metric_prefix=MetricPrefix.Micro)
nanoampere = nA = Ampere(metric_prefix=MetricPrefix.Nano)
kiloampere = kA = Ampere(metric_prefix=MetricPrefix.Kilo)
abampere = abA = FundamentalCurrentUnit(name="abampere", symbol="abA", amperes_per_unit=10)
statampere = statA = FundamentalCurrentUnit(name="statampere", symbol="statA", amperes_per_unit=3.33564e-10)