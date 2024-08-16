from .unit import Unit
from .fundamental_unit import FundamentalQuantityUnit

class Measurement:
    """ Measurement Class
    
    Represents a measurement with a value and a unit.
    
    Attributes:
        value (float): The value of the measurement.
        unit (Unit): The unit of the measurement.
        
    Examples:
        >>> from ucalcx import Measurement, Unit
        >>> length = Unit.from_fundamental_units((Unit.meter, 1,))
        >>> length_measurement = Measurement(5, length)
        >>> length_measurement
        Measurement(5, Unit({length: FQUnit(meter, m, length), power: 1}))
    """
    
    def __init__(self, value: float, unit: Unit):
        self.value = value
        if isinstance(unit, FundamentalQuantityUnit):
            unit = Unit.from_fundamental_units((unit, 1,))
        elif not isinstance(unit, Unit):
            raise ValueError("The unit must be a Unit or a FundamentalQuantityUnit")
        self.unit = unit

    def convert_to(self, other: Unit) -> "Measurement":
        """ Convert the measurement to a new unit. """
        
        return Measurement(value=self.unit.convert_to(other, self.value), unit=other)
    
    def __str__(self):
        return f"{self.value} {self.unit.symbol}"
    
    def __add__(self, other: "Measurement") -> "Measurement":
        # This will throw a ValueError if the units are incompatible
        others_converted = other.unit.convert_to(self.unit, other.value)

        return Measurement(value=self.value + others_converted, unit=self.unit)
    
    def __sub__(self, other: "Measurement") -> "Measurement":
        # This will throw a ValueError if the units are incompatible
        others_converted = other.unit.convert_to(self.unit, other.value)

        return Measurement(value=self.value - others_converted, unit=self.unit)
    
    def __mul__(self, other: "Measurement") -> "Measurement":
        # Convert all components that are shared to a common unit in that dimension
        new_value = other.value
        for component in self.unit.components:
            other_component = other.unit.dimension[component['unit'].quantity]
            if other_component is not None and other_component['power'] != 0:
                new_value = other.value ** (1/other_component['power'])
                new_value = other_component['unit'].convert_to(component['unit'], new_value) ** other_component['power']
        return Measurement(value=self.value * new_value, unit=self.unit * other.unit)


    def __truediv__(self, other: "Measurement") -> "Measurement":
        # Convert all components that are shared to a common unit in that dimension
        new_value = other.value
        for component in self.unit.components:
            other_component = other.unit.dimension[component['unit'].quantity]
            if other_component is not None and other_component['power'] != 0:
                new_value = other.value ** (1/other_component['power'])
                new_value = other_component['unit'].convert_to(component['unit'], new_value) ** other_component['power']
        return Measurement(value=self.value / new_value, unit=self.unit / other.unit)

    def __repr__(self):
        return f"Measurement({self.value}, {self.unit})"
