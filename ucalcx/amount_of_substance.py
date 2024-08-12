from common import FundamentalQuantityUnit, FundamentalQuantity, MetricPrefix
from abc import abstractmethod, ABC

class FundamentalAmountUnit(FundamentalQuantityUnit, ABC):
    def __init__(self, name: str, symbol: str):
        super().__init__(name=name, symbol=symbol, quantity=FundamentalQuantity.Current)

    def _conversion_method(self, other: "FundamentalAmountUnit", value: float) -> float:
        if not isinstance(other, FundamentalAmountUnit):
            raise ValueError(f"Tried to convert {self} to {other}. Expected two amount of substance units.")
                
        return value * self.moles_per_unit() / other.moles_per_unit()

    @abstractmethod
    def moles_per_unit(self) -> float:
        pass
            

class Mole(FundamentalAmountUnit):
    def __init__(self, metric_prefix: MetricPrefix=MetricPrefix.Base):
        super().__init__(name="mole", symbol="mol")
        self.metric_prefix = metric_prefix

    def moles_per_unit(self) -> float:
        return 10 ** self.metric_prefix.exponent

    @property
    def name(self) -> str:
        return f"{self.metric_prefix.name}{super().name}" 
    
    @property
    def symbol(self) -> str:
        return f"{self.metric_prefix.symbol}{super().symbol}"
    

mole = mol = Mole()
millimole = mmol = Mole(metric_prefix=MetricPrefix.Milli)
micromole = umol = Mole(metric_prefix=MetricPrefix.Micro)
nanomole = nmol = Mole(metric_prefix=MetricPrefix.Nano)
kilomole = kmol = Mole(metric_prefix=MetricPrefix.Kilo)
