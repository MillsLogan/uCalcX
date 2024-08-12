from .quantity import FundamentalQuantity
from .fundamental_unit import FundamentalQuantityUnit
from typing import Union
from copy import deepcopy


class Unit:
    def __init__(self, dimension: dict[FundamentalQuantity, FundamentalQuantityUnit]=dict()):
        self.dimension: dict[FundamentalQuantity, FundamentalQuantityUnit] = dimension
        self.dimension.update({quantity: None for quantity in FundamentalQuantity if quantity not in self.dimension})
    
    @classmethod
    def from_fundamental_units(cls, *components: FundamentalQuantityUnit) -> "Unit":
        dimensions = {quantity: None for quantity in FundamentalQuantity}
        for component in components:
            if dimensions[component.quantity] is not None:
                raise ValueError(f"Cannot have multiple components for the same quantity: {component.quantity}")
            dimensions[component.quantity] = component
        return cls(dimensions)
    
    def copy(self) -> "Unit":
        return deepcopy(self)

    @property
    def components(self) -> list[FundamentalQuantity]:
        return [component for component in self.dimension.values() if component is not None]

    @property
    def name(self) -> str:
        numerator = []
        denominator = []
        for component in self.components:
            if component is None:
                continue
            if component.power > 0:
                numerator.append(component.name)
            elif component.power < 0:
                denominator.append(component.name.replace("-", ""))
                if component.power == -1:
                    denominator[-1] = denominator[-1][:-2] # Remove ^1 from the string
        if not numerator and not denominator:
            numerator.append("1")
        return f"{'*'.join(numerator)}{'/' + '*'.join(denominator) if denominator else ''}".replace("-", "")

    @property
    def symbol(self) -> str:
        numerator = []
        denominator = []
        for component in self.components:
            if component is None:
                continue
            if component.power > 0:
                numerator.append(component.symbol)
            elif component.power < 0:
                denominator.append(component.symbol.replace("-", ""))
                if component.power == -1:
                    denominator[-1] = denominator[-1][:-2] # Remove ^1 from the string
        if not numerator and not denominator:
            numerator.append("1")
        return f"{'*'.join(numerator)}{'/' + '*'.join(denominator) if denominator else ''}".replace("-", "")
    
    def convert_to(self, other: "Unit", value: float) -> float:
        for component in self.components:
            other_component = other.dimension[component.quantity]
            if other_component is None:
                raise ValueError(f"Cannot convert {self} to {other}. {component.quantity} is missing from the target unit.")
            elif not component.can_convert_to(other_component):
                raise ValueError(f"Cannot convert {self} to {other}. {component.quantity} is incompatible.")
            else:
                value = component.convert_to(other_component, value)
        return value


    def __str__(self):
        return f"{self.name} ({self.symbol})"
                
    def __mul__(self, other: Union[FundamentalQuantityUnit, "Unit"]) -> "Unit":
        new_unit = self.copy()
        if isinstance(other, FundamentalQuantityUnit):
            if self.dimension[other.quantity] is not None:
                new_unit.dimension[other.quantity] = self.dimension[other.quantity] * other
            else:
                new_unit.dimension[other.quantity] = other
        elif isinstance(other, Unit):
            for component in other.components:
                if self.dimension[component.quantity] is not None:
                    new_unit.dimension[component.quantity] = self.dimension[component.quantity] * component
                else:
                    new_unit.dimension[component.quantity] = component
        else:
            raise ValueError("Cannot multiply a unit by a non-unit")
        
        return new_unit
    
    def __truediv__(self, other: Union[FundamentalQuantityUnit, "Unit"]) -> "Unit":
        new_unit = self.copy()
        if isinstance(other, FundamentalQuantityUnit):
            if new_unit.dimension[other.quantity] is not None:
                new_unit.dimension[other.quantity] = self.dimension[other.quantity] / other
                if new_unit.dimension[other.quantity].power == 0:
                    new_unit.dimension[other.quantity] = None
            else:
                new_unit.dimension[other.quantity] = other.with_power(-other.power)
        elif isinstance(other, Unit):
            for component in other.components:
                if self.dimension[component.quantity] is not None:
                    new_unit.dimension[component.quantity] = self.dimension[component.quantity] / component
                    if new_unit.dimension[component.quantity].power == 0:
                        new_unit.dimension[component.quantity] = None
                else:
                    new_unit.dimension[component.quantity] = component.with_power(-component.power)
        else:
            raise ValueError("Cannot divide a unit by a non-unit")
        
        return new_unit
    
