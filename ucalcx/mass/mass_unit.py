from common import FundamentalQuantityUnit, FundamentalQuantity
from abc import abstractmethod, ABC

class FundamentalMassUnit(FundamentalQuantityUnit, ABC):
    def __init__(self, name: str, symbol: str):
        super().__init__(name=name, symbol=symbol, quantity=FundamentalQuantity.Mass)

    def _conversion_method(self, other: "FundamentalMassUnit", value: float) -> float:
        if not isinstance(other, FundamentalMassUnit):
            raise ValueError(f"Tried to convert {self} to {other}. Expected two mass units.")
                
        return value * self.grams_per_unit() / other.grams_per_unit()

    @abstractmethod
    def grams_per_unit(self) -> float:
        pass
            