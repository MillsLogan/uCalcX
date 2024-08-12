from .quantity import FundamentalQuantity
from typing import Self
from abc import ABC, abstractmethod
from copy import deepcopy
from typing import Union


class FundamentalQuantityUnit(ABC):
    def __init__(self, name: str, symbol: str, quantity: FundamentalQuantity, power: int=1):
        self._name = name
        self._symbol = symbol
        self.quantity = quantity
        
        if power == 0:
            raise ValueError("Cannot have a unit for a unitless quantity")
        elif not isinstance(power, int):
            raise ValueError("The power of a unit must be an integer")
        
        self.power = power

    def with_power(self, power: int) -> Self:
        new_copy = deepcopy(self)
        new_copy.power = power
        return new_copy

    def can_convert_to(self, other: Self) -> bool:
        return self.quantity == other.quantity and self.power == other.power

    def convert_to(self, other: Self, value: float) -> float:
        if self.quantity != other.quantity:
            raise ValueError(F"Cannot convert {self.quantity} to {other.quantity}")
        return self._conversion_method(other=other, value=value)
        
    @property
    def name(self) -> str:
        return f"{self._name}{'^'+str(self.power) if self.power != 1 else ''}"
    
    @property
    def symbol(self) -> str:
        return f"{self._symbol}{'^'+str(self.power) if self.power != 1 else ''}"
        
    @abstractmethod
    def _conversion_method(self, other: Self, value: float) -> float:
        pass

    def __str__(self):
        return f"{self.name} ({self.symbol})"
    
    def __pow__(self, power: int) -> "FundamentalQuantityUnit":
        if not isinstance(power, int):
            raise ValueError("The power of a unit must be an integer")
        return self.with_power(power)
    
    def __rmul__(self, other: int) -> "Unit":
        if not isinstance(other, (int, float)):
            raise ValueError("Cannot multiply a unit by a non-numeric value")
        
        raise NotImplementedError("The multiplication of a unit by a scalar is not yet implemented")
    
    def __mul__(self, other: Union[Self | "Unit"]) -> "Unit":
        from .unit import Unit
        if not isinstance(other, FundamentalQuantityUnit):
            raise ValueError("Cannot multiply a unit by a non-unit")
        
        if self.quantity == other.quantity:
            new_power = self.power + other.power
            return self.with_power(new_power)
        return Unit.from_fundamental_units(self, other)

    def __truediv__(self, other: Self) -> "Unit":
        from .unit import Unit
        if not isinstance(other, FundamentalQuantityUnit):
            raise ValueError("Cannot divide a unit by a non-unit")
        
        if self.quantity == other.quantity:
            return self.with_power(self.power - other.power)
        return Unit.from_fundamental_units(self, other.with_power(other.power * -1))

    def __div__(self, other: Self) -> "Unit":
        return self.__truediv__(other)