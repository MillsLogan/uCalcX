from .quantity import FundamentalQuantity
from typing import Self
from abc import ABC, abstractmethod
from copy import deepcopy


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

    def with_power(self, power: int):
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
    
    def __str__(self):
        return f"{self.name} ({self.symbol})"
        
    @abstractmethod
    def _conversion_method(self, other: Self, value: float) -> float:
        pass


class QuantityComponent:
    def __init__(self, value: float, unit: FundamentalQuantityUnit):
        self.value: float = value
        self.unit: FundamentalQuantityUnit = unit
        
    @property
    def quantity(self) -> FundamentalQuantity:
        return self.unit.quantity
    
    @property
    def power(self) -> int:
        return self.unit.power

    def can_convert_to(self, other: FundamentalQuantityUnit) -> bool:
        # This will bypass the power check - may need to be changed later as it may cause confusion
        if self.quantity != other.quantity:
            return False
        elif self.power != other.power:
            return False
        return True
    
    def convert_to(self, other: FundamentalQuantityUnit) -> Self:
        if not isinstance(other, FundamentalQuantityUnit):
            raise ValueError("Cannot convert to a non-FundamentalQuantityUnit")

        if not self.can_convert_to(other):
            raise ValueError(f"Cannot convert {self} to {other}, because of mismatching quantities and/or powers")
        
        return self.__class__(value=self.unit.convert_to(other, self.value), unit=other)
        
    def __str__(self):
        return f"{self.value} {self.unit.symbol}{'^'+str(self.power) if self.power != 1 else ''}"
