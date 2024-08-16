from .quantity import FundamentalQuantity
from typing import Self
from abc import ABC, abstractmethod
from typing import Union, Optional
from ..exceptions import IncompatibleUnitsError, InvalidValueError


class FundamentalQuantityUnit(ABC):
    """A base class for units of fundamental quantities. This class should not be instantiated directly.
    Instead, use one of the subclasses that inherit from this class.

    Args:
        name (str): The name of the unit (e.g. meter, second, etc.)
        symbol (str): The symbol of the unit (e.g. m for meters, s for seconds, etc.)
        quantity (FundamentalQuantity): The quantity that the unit represents (e.g. length, time, etc.)
    """

    def __init__(self, name: str, symbol: str, quantity: FundamentalQuantity):
        """ Initializes a new instance of the FundamentalQuantityUnit class. """

        self._name = name
        self._symbol = symbol
        self.quantity = quantity

    def can_convert_to(self, other: Self) -> bool:
        """ Check if the unit can be converted to another unit. 
        
        Units can be converted if they represent the same physical quantity (e.g. length, time, etc.). 
        For example, meters can be converted to kilometers, but not to seconds. 
        """

        if not isinstance(other, FundamentalQuantityUnit):
            return False

        return self.quantity == other.quantity

    def convert_to(self, other: Self, value: float) -> float:
        """ Convert a value from this unit to another unit. 
        
        Args:
            other (FundamentalQuantityUnit): The unit to convert to.
            value (float): The value to convert.

        Returns:
            float: The converted value.

        Raises:
            IncompatibleUnitsError: If the units represent different quantities.

        Examples:
            >>> meter.convert_to(kilometer, 1000) # Convert 1000 meters to kilometers
            1.0
        """

        if self.quantity != other.quantity:
            raise IncompatibleUnitsError(f"Cannot convert {self.name} to {other.name}, as they represent different "\
                                         f"quantities, {self.quantity} and {other.quantity} respectively.")
        return self._conversion_method(other=other, value=value)
        
    @property
    def name(self) -> str:
        """ Get the name of the unit. """

        return f"{self._name}"
    
    @property
    def symbol(self) -> str:
        """ Get the symbol of the unit. """

        return f"{self._symbol}"
        
    @abstractmethod
    def _conversion_method(self, other: Self, value: float) -> float:
        """ An abstract method that should be implemented by subclasses to convert a value from this unit to another unit.
        This is commonly done by defining some base unit (e.g. meters, seconds, etc.) and converting to and from that unit.
        See the length and time modules for examples of how this method is implemented. 
        
        Args:
            other (FundamentalQuantityUnit): The unit to convert to.
            value (float): The value to convert.

        Returns:
            float: The converted value.
        """

        pass

    def __repr__(self):
        return f"FQUnit({self.name}, {self.symbol}, {self.quantity})"

    def __str__(self):
        return f"{self.name} ({self.symbol})"
    
    def __pow__(self, power: int) -> "Unit":
        """ Creates a new `Unit` instance by raising this base unit to the specified power. 
        
        Args:
            power (int): The power to raise the unit to.

        Returns:
            Unit: A new unit instance with the specified power.

        Raises:
            InvalidValueError: If the power is not an integer.

        Examples:
            >>> from ucalcx.length import meter
            >>> meter
            FQUnit(meter, m, length)
            >>> meter ** 2  # Square meters
            Unit({length: FQUnit(meter, m, length), power: 2}) 
        """

        if not isinstance(power, int):
            raise InvalidValueError("The power of a unit must be an integer")
        from .unit import Unit
        return Unit.from_fundamental_units((self, power,))
    
    def __rmul__(self, other: int | float) -> "Measurement":
        """ Add a unit to a scalar value, by multiplying the scalar value by this unit. 
        
        Args: 
            other (int): The scalar value to multiply by the unit.

        Returns:
            Measurement: A new measurement instance with the specified value and unit.

        Raises:
            ValueError: If the other value is not a numeric value.

        Examples:
            >>> from ucalcx.length import meter
            >>> 2 * meter
            Measurement(2, Unit({length: FQUnit(meter, m, length), power: 1}))
        """

        from .measurement import Measurement
        if not isinstance(other, (int, float)):
            raise ValueError("Cannot multiply a unit by a non-numeric value")
        
        return Measurement(other, self)
    
    def __mul__(self, other: Union[Self | "Unit"]) -> "Unit":
        """ Multiply this unit by another unit.

        This operation will ignore the unit of the other value if it is of the same quantity as this unit.
        For example, multiplying meters by meters will result in square meters, and multiplying meters 
        by kilometers will also result in square meters. This is the behavior across the entire library, 
        the left-hand side unit is always the one that determines the unit of the result if the units are ambiguous.
        
        Args:
            other (Union[FundamentalQuantityUnit, Unit]): The unit to multiply by.
            
        Returns:
            Unit: A new unit instance representing the product of the two units.
        """

        from .unit import Unit
        if not isinstance(other, (Unit, FundamentalQuantityUnit)):
            raise InvalidValueError(f"Expected a unit or a fundamental quantity unit, but got {other} of type {type(other)}")
        
        if isinstance(other, FundamentalQuantityUnit):
            print("?")
            if self.quantity == other.quantity:
                return Unit.from_fundamental_units((self, 2,))
            return Unit.from_fundamental_units((self, 1,), (other, 1,))
        
        # Call __mul__ on the Unit class
        print("Calling __mul__ on the Unit class")
        return other * self

    def __truediv__(self, other: Union[Self | "Unit"]) -> Optional["Unit"]:
        """ Divide this unit by another unit. 
        
        If the units are of the same quantity, None will be returned, because the result would be unitless.
        
        Args:
            other (Union[FundamentalQuantityUnit, Unit]): The unit to divide by.
        
        Returns:
            Unit: A new unit instance representing the division of the two units.

        """

        from .unit import Unit
        if not isinstance(other, (FundamentalQuantityUnit, Unit)):
            raise InvalidValueError(f"Expected a unit or a fundamental quantity unit, but got {other} of type {type(other)}")
        
        if isinstance(other, FundamentalQuantityUnit):
            if self.quantity == other.quantity:
                return None
            return Unit.from_fundamental_units((self, 1,), (other, -1,))
        else:
            return other.__rtruediv__(self)

    def __div__(self, other: Self) -> "Unit":
        """ Divide this unit by another unit. 
        
        If the units are of the same quantity, None will be returned, because the result would be unitless.
        
        Args:
            other (Union[FundamentalQuantityUnit, Unit]): The unit to divide by.
        
        Returns:
            Unit: A new unit instance representing the division of the two units.
        """

        return self.__truediv__(other)