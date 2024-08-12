from .unit import Unit
from .fundamental_unit import FundamentalQuantityUnit

class Measurement:
    def __init__(self, value: float, unit: Unit):
        self.value = value
        if isinstance(unit, FundamentalQuantityUnit):
            unit = Unit.from_fundamental_units(unit)
        elif not isinstance(unit, Unit):
            raise ValueError("The unit must be a Unit or a FundamentalQuantityUnit")
        self.unit = unit

    def convert_to(self, other: Unit) -> "Measurement":
        return Measurement(value=self.unit.convert_to(other, self.value), unit=other)
    
    def __str__(self):
        return f"{self.value} {self.unit.symbol}"
    
    def __add__(self, other: "Measurement") -> "Measurement":
        # This will throw a ValueError if the units are incompatible
        others_converted = other.unit.convert_to(self.unit, other.value)

        return Measurement(value=self.value + others_converted, unit=self.unit)
    
    def __sub__(self, other: "Measurement") -> "Measurement":
        # This will throw a ValueError if the units are incompatible
        others_converted = other.convert_to(self.unit, other.value)

        return Measurement(value=self.value - others_converted, unit=self.unit)
    
    def __mul__(self, other: "Measurement") -> "Measurement":
        # Convert all components that are shared to a common unit in that dimension
        new_value = other.value
        for component in self.unit.components:
            other_component = other.unit.dimension[component.quantity]
            if other_component is not None:
                new_value = other_component.convert_to(component.with_power(other_component.power), other.value)
        return Measurement(value=self.value * new_value, unit=self.unit * other.unit)


    def __truediv__(self, other: "Measurement") -> "Measurement":
        # Convert all components that are shared to a common unit in that dimension
        new_value = other.value
        for component in self.unit.components:
            other_component = other.unit.dimension[component.quantity]
            if other_component is not None:
                new_value = other_component.convert_to(component.with_power(other_component.power), other.value)
        return Measurement(value=self.value / new_value, unit=self.unit / other.unit)
