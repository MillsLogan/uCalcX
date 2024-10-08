from ..common import FundamentalQuantityUnit, FundamentalQuantity
from abc import abstractmethod, ABC

class FundamentalLengthUnit(FundamentalQuantityUnit, ABC):
    """ A base class for units of length. This class should not be instantiated directly.
    
    Instead, use one of the subclasses that inherit from this class.
    
    Args:
        name (str): The name of the unit (e.g. meter, inch, etc.)
        symbol (str): The symbol of the unit (e.g. m for meters, in for inches, etc.)
    """
    
    def __init__(self, name: str, symbol: str):
        super().__init__(name=name, symbol=symbol, quantity=FundamentalQuantity.Length)

    def _conversion_method(self, other: "FundamentalLengthUnit", value: float) -> float:
        if not isinstance(other, FundamentalLengthUnit):
            raise ValueError(f"Tried to convert {self} to {other}. Expected two length units.")
                
        return value * self.meters_per_unit() / other.meters_per_unit()

    @abstractmethod
    def meters_per_unit(self) -> float:
        pass
            