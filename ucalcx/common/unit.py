from .quantity import FundamentalQuantity
from .fundamental_unit import FundamentalQuantityUnit
from typing import Union, Self
from ..exceptions import IncompatibleUnitsError, InvalidUnitError, InvalidOperationError, InvalidValueError


DimensionValue = dict["unit": FundamentalQuantityUnit, "power": int]
" A type alias for a dictionary that represents a dimension value in a unit. "


class Unit:
    """ A class that represents a unit of measurement.

    Attributes:
        dimension (dict[FundamentalQuantity: DimensionValue]): A dictionary that represents the dimensions of the unit.

    Examples:
        >>> from ucalcx.common import Unit
        >>> from ucalcx.length import meter, kilometer
        >>> from ucalcx.time import second
        >>> meter / second
        Unit(meter/second (m/s))
        >>> meter / kilometer
        Unit(length (m/km))
    """

    def __init__(self, dimension: dict[FundamentalQuantity: DimensionValue]=dict()):
        self.dimension: dict[FundamentalQuantity: DimensionValue] = dimension
        self.dimension.update({quantity: {"unit": None, "power": 0} for quantity in FundamentalQuantity if quantity not in self.dimension})
    
    @classmethod
    def from_fundamental_units(cls, *units_and_powers: tuple[FundamentalQuantityUnit, int]) -> Self:
        """ Create a new unit from a list of fundamental units and their powers. 
        
        Args:
            *units_and_powers (tuple[FundamentalQuantityUnit, int]): A list of tuples that contain a fundamental unit and a power.
            
        Returns:
            Unit: The new unit.
            
        Raises:
            InvalidUnitError: If a unit is not a valid unit.
            InvalidValueError: If a power is not an integer.
        
        Examples:
            >>> from ucalcx.common import Unit
            >>> from ucalcx.length import meter
            >>> from ucalcx.time import second
            >>> Unit.from_fundamental_units((meter, 1), (second, -1))
            Unit(meter / second (m/s))
        """

        dimensions = {}
        for unit, power in units_and_powers:
            if not isinstance(unit, FundamentalQuantityUnit):
                raise InvalidUnitError(f"{unit} is not a valid unit.")
            if not isinstance(power, int):
                raise InvalidValueError(f"The power of a unit must be an integer, not {power} of type {type(power)}.")
            if power == 0 and unit is not None:
                dimensions[unit.quantity] = {"unit": None, "power": 0}
            elif unit is not None and unit.quantity in dimensions:
                dimensions[unit.quantity]["power"] += power
            else:
                dimensions[unit.quantity] = {"unit": unit, "power": power}
        return cls(dimensions)

    @property
    def components(self) -> list[FundamentalQuantity]:
        return [component for component in self.dimension.values() if component["unit"] is not None and component["power"] != 0]

    @property
    def name(self) -> str:
        """ The name of the unit. Joined by '*' for the numerator and '/' for the denominator. """

        numerator = []
        denominator = []
        for component in self.components:
            if component["power"] > 0:
                numerator.append(component["unit"].name + (f"^{component['power']}" if component["power"] != 1 else ""))
            elif component["power"] < 0:
                denominator.append(component["unit"].name + (f"^{component['power']}" if component["power"] != -1 else ""))
        return f"{'*'.join(numerator)}{'/' + '*'.join(denominator) if denominator else ''}".replace("-", "")

    @property
    def symbol(self) -> str:
        """ The symbol of the unit. Joined by '*' for the numerator and '/' for the denominator. """

        numerator = []
        denominator = []
        for component in self.components:
            if component["power"] > 0:
                numerator.append(component["unit"].symbol + (f"^{component['power']}" if component["power"] != 1 else ""))
            elif component["power"] < 0:
                denominator.append(component["unit"].symbol + (f"^{component['power']}" if component["power"] != -1 else ""))
        return f"{'*'.join(numerator)}{'/' + '*'.join(denominator) if denominator else ''}".replace("-", "")
    
    def convert_to(self, other: "Unit", value: float) -> float:
        """ Convert a value from this unit to another unit.

        Args:
            other (Unit): The unit to convert to.
            value (float): The value to convert.

        Returns:
            float: The converted value.

        Raises:
            IncompatibleUnitsError: If the units are incompatible.
            InvalidUnitError: If the other unit is not a valid unit.

        Examples:
            >>> from ucalcx.common import Unit
            >>> from ucalcx.length import meter, kilometer
            >>> velocity = meter / second
            >>> velocity.convert_to(kilometer / hour, 1)
            3.6
        """

        if isinstance(other, FundamentalQuantityUnit):
            if self.dimension[other.quantity] is None:
                raise IncompatibleUnitsError(f"Cannot convert {self} to {other}. {other.quantity} is missing from the source unit.")
            elif len(self.components) > 1:
                raise IncompatibleUnitsError(f"Cannot convert {self} to {other}. The source unit has multiple components.")
            elif self.dimension[other.quantity]["power"] != 1:
                raise IncompatibleUnitsError(f"Cannot convert {self} to {other}. {self.dimension[other.quantity]} is not a fundamental unit, having a power of {self.dimension[other.quantity]['power']}.")
            return self.dimension[other.quantity]["unit"].convert_to(other, value)
        elif isinstance(other, Unit):
            for component in self.components:
                other_component = other.dimension[component["unit"].quantity]
                if other_component is None:
                    raise IncompatibleUnitsError(f"Cannot convert {self} to {other}. {component["unit"].quantity} is missing from the target unit.")
                elif not component["unit"].can_convert_to(other_component["unit"]):
                    raise IncompatibleUnitsError(f"Cannot convert {self} to {other}. {component["unit"].quantity} is incompatible.")
                elif component["power"] != other_component["power"]:
                    raise IncompatibleUnitsError(f"Cannot convert {self} to {other}. {component["unit"].quantity} has a power of {component["power"]} in the source unit and {other_component["power"]} in the target unit.")
                value = component["unit"].convert_to(other_component["unit"], value)
            return value
        else:
            raise InvalidUnitError(f"{other} is not a valid unit, has type {type(other)}.")


    def __str__(self):
        return f"{self.name} ({self.symbol})"
                
    def __mul__(self, other: Union[FundamentalQuantityUnit, "Unit"]) -> "Unit":
        """ Multiply the unit by another unit or a fundamental unit.
        
        Args:
            other (Union[FundamentalQuantityUnit, Unit]): The unit to multiply by.
            
        Returns:
            Unit: The new unit.
            
        Raises:
            InvalidOperationError: If the other value is not a unit.
        """

        new_unit = Unit(dict(self.dimension))
        if isinstance(other, FundamentalQuantityUnit):
            for quantity in FundamentalQuantity:
                if other.quantity == quantity:
                    new_unit.dimension[quantity]["power"] = 1 + self.dimension[quantity]["power"]
                    new_unit.dimension[quantity]["unit"] = other if self.dimension[quantity]["unit"] is None else self.dimension[quantity]["unit"]
        elif isinstance(other, Unit):
            for quantity in FundamentalQuantity:
                if other.dimension[quantity]["unit"] is not None:
                    new_unit.dimension[quantity]["unit"] = other.dimension[quantity]["unit"]
                    new_unit.dimension[quantity]["power"] += other.dimension[quantity]["power"]
        else:
            raise InvalidOperationError("Cannot multiply a unit by a non-unit, has type {type(other)}, moving the unit to the right side of the multiplication operation, with a scalar value will result in a measurment object.")
        
        return new_unit
    
    def __truediv__(self, other: Union[FundamentalQuantityUnit, "Unit"]) -> "Unit":
        """ Divide the unit by another unit or a fundamental unit.

        Args:
            other (Union[FundamentalQuantityUnit, Unit]): The unit to divide by.

        Returns:
            Unit: The new unit.

        Raises:
            InvalidOperationError: If the other value is not a unit.
        """

        new_unit = Unit(dict(self.dimension))
        if isinstance(other, FundamentalQuantityUnit):
            new_unit.dimension[other.quantity]["power"] -= 1
        elif isinstance(other, Unit):
            for quantity in FundamentalQuantity:
                if other.dimension[quantity]["unit"] is not None:
                    new_unit.dimension[quantity]["unit"] = other.dimension[quantity]["unit"]
                    new_unit.dimension[quantity]["power"] -= other.dimension[quantity]["power"]
                if new_unit.dimension[quantity]["power"] == 0:
                    new_unit.dimension[quantity]["unit"] = None
        else:
            raise InvalidOperationError("Cannot multiply a unit by a non-unit, has type {type(other)}, moving the unit to the right side of the multiplication operation, with a scalar value will result in a measurment object.")
        
        return new_unit
    
    def __rmul__(self, other: float | int) -> "Measurement":
        """ Multiply the unit by a scalar value.
        
        Args:
            other (float | int): The scalar value to multiply by.
            
        Returns:
            Measurement: The new measurement.
        """
        
        from .measurement import Measurement
        return Measurement(other, self)
    
    def __repr__(self) -> str:
        return f"Unit({['(' + component['unit'].__repr__() + '^' + str(component['power']) + ')'  for component in self.dimension.values() if component['unit'] is not None]})"