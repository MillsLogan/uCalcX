from common import FundamentalQuantityUnit, FundamentalQuantity
from abc import abstractmethod, ABC

class FundamentalLengthUnit(FundamentalQuantityUnit, ABC):
    def __init__(self, name: str, symbol: str, power: int=1):
        super().__init__(name=name, symbol=symbol, quantity=FundamentalQuantity.Length, power=power)

    def _conversion_method(self, other: "FundamentalLengthUnit", value: float) -> float:
        if not isinstance(other, FundamentalLengthUnit):
            raise ValueError(f"Tried to convert {self} to {other}. Expected two length units.")
        
        this_to_other_factor = self.meters_per_unit() / other.meters_per_unit()
        
        return value * (this_to_other_factor ** self.power)

    @abstractmethod
    def meters_per_unit(self) -> float:
        pass
            