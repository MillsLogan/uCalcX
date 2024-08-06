from dataclasses import dataclass


@dataclass(frozen=True, eq=True)
class Measurement:
    """
    # Measurement Class

    Represents a measurement consisting of a numerical value and a unit of measurement. This class allows for the representation and manipulation of measurements with different units.

    Attributes:
        value (float): The numerical value of the measurement.
        unit (Unit): The unit associated with the measurement.

    ## Methods:
        convert_to(other_unit: Unit) -> Measurement:
            Converts the measurement to the specified `other_unit`. This method checks that the `other_unit` measures the same physical quantity as the current unit, performs the conversion, and returns a new `Measurement` object with the converted value.
    """
    
    value: float
    """ The value of the measurement. """
    
    unit: 'Unit'
    """ The unit of the measurement. """
    
    def convert_to(self, other: 'Unit') -> 'Measurement':
        """
        Converts the measurement to the specified `other_unit`.

        This method:
        1. Asserts that the `other_unit` measures the same physical quantity as the current unit.
        2. Calls `self.unit.convert_to(other_unit, self.value)` to perform the conversion.
        3. Creates and returns a new `Measurement` object with the converted value and `other_unit` as the unit.

        Args:
            other_unit (Unit): The target unit to convert the measurement to.

        Returns:
            Measurement: A new `Measurement` object with the converted value and the target unit.

        Raises:
            ValueError: If the `other_unit` measures a different physical quantity than the current unit.
        """
        
        if other.quantity != self.unit.quantity:
            raise ValueError(f"Cannot convert {self.unit.quantity.name} to {other.quantity.name}.")
        
        converted_value = self.unit.convert_to(other, self.value)
        return Measurement(converted_value, other)
    
    def add_scalar(self, scalar: float | int) -> 'Measurement':
        """
        Adds a scalar value to the current measurement.

        This method creates a new `Measurement` object with the result of adding the scalar value to the current measurement's value. The unit of the measurement remains unchanged.

        Args:
            scalar (float | int): The scalar value to add to the measurement. Must be a number.

        Returns:
            Measurement: A new `Measurement` object with the updated value.

        Raises:
            ValueError: If the scalar is not a number.

        Example:
            >>> from ucalcx import Measurement, MetricPrefix
            >>> from ucalcx.length.metric import Meter
            >>> fifty_meters = Measurement(50, Meter())
            >>> new_length = fifty_meters.add_scalar(3)
            >>> print(new_length.value)
            53
            >>> one_kilometer = Measurement(1, Meter(MetricPrefix.Kilo))
            >>> new_length = one_kilometer.add_scalar(2) # Notice this does 1 + 2, not 1000 + 2
            >>> print(new_length.value) 
            3
        """

        if isinstance(scalar, (int, float)):
            return Measurement(self.value + scalar, self.unit)
        else:
            raise ValueError("Only scalar values can be added using add_scalar method, consider using + or add_measurement.")
        
    def add_measurement(self, other: 'Measurement') -> 'Measurement':
        """
        Adds another `Measurement` object to the current measurement.

        This method performs addition between two `Measurement` objects by converting the other measurement to the unit of the current measurement. The result is a new `Measurement` object with the sum of the values.

        Args:
            other (Measurement): The `Measurement` object to add. Its unit must be compatible with the current measurement's unit.

        Returns:
            Measurement: A new `Measurement` object with the updated value.

        Raises:
            ValueError: If the units of the measurements are incompatible.

        Example:
            >>> from ucalcx import Measurement, MetricPrefix
            >>> from ucalcx.length.metric import Meter
            >>> fifty_meters = Measurement(50, Meter())
            >>> one_kilometer = Measurement(1, Meter(MetricPrefix.Kilo))
            >>> new_length = fifty_meters.add_measurement(one_kilometer) # Notice this does 50 + 1000, not 50 + 1
            >>> print(new_length) # Maintains the unit of the calling object
            1050 m
        """

        return self + other
    
    def sub_measurement(self, other: 'Measurement') -> 'Measurement':
        """
        Subtracts another `Measurement` object from the current measurement.

        This method performs subtraction between two `Measurement` objects by converting the other measurement to the unit of the current measurement. The result is a new `Measurement` object with the difference of the values.

        Args:
            other (Measurement): The `Measurement` object to subtract. Its unit must be compatible with the current measurement's unit.

        Returns:
            Measurement: A new `Measurement` object with the updated value.

        Raises:
            ValueError: If the units of the measurements are incompatible.

        Example:
            >>> from ucalcx import Measurement, MetricPrefix
            >>> from ucalcx.length.imperial import Foot, Yard
            >>> five_yards = Measurement(5, Yard())
            >>> three_feet = Measurement(3, Foot()) # 1 yard = 3 feet
            >>> new_length = five_yards.sub_measurement(three_feet) # Notice this does 5 - 1, not 5 - 3
            >>> print(new_length) # Maintains the unit of the calling object
            4 yd
        """

        return self - other
    
    def sub_scalar(self, scalar: float | int) -> 'Measurement':
        """
        Subtracts a scalar value from the current measurement.

        This method creates a new `Measurement` object with the result of subtracting the scalar value from the current measurement's value. The unit of the measurement remains unchanged.

        Args:
            scalar (float | int): The scalar value to subtract from the measurement. Must be a number.

        Returns:
            Measurement: A new `Measurement` object with the updated value.

        Raises:
            ValueError: If the scalar is not a number.

        Example:
            >>> from ucalcx import Measurement, MetricPrefix
            >>> from ucalcx.length.imperial import Mile
            >>> one_mile = Measurement(1, Mile())
            >>> new_length = one_mile.sub_scalar(0.5)
            >>> print(new_length)
            0.5 mi
        """

        if isinstance(scalar, (int, float)):
            return Measurement(self.value - scalar, self.unit)
        else:
            raise ValueError("Only scalar values can be subtracted using sub_scalar method, consider using - or sub_measurement.")

    def mul_scalar(self, scalar: float | int) -> 'Measurement':
        """
        Multiplies the current measurement by a scalar value. **The unit of measurement remains UNCHANGED.**

        This method creates a new `Measurement` object with the result of multiplying the current measurement's value by the scalar. **The unit of the measurement remains unchanged.**

        Args:
            scalar (float | int): The scalar value to multiply the measurement by. Must be a number.

        Returns:
            Measurement: A new `Measurement` object with the updated value.

        Raises:
            ValueError: If the scalar is not a number.

       Example:
            >>> from ucalcx import Measurement, MetricPrefix
            >>> from ucalcx.length.imperial import Mile
            >>> two_miles = Measurement(2, Mile())
            >>> four_miles = two_miles.mul_scalar(2)
            >>> print(four_miles) # Note that the unit is maintained i.e. still miles not square miles
            4 mi
        """

        if isinstance(scalar, (int, float)):
            return Measurement(self.value * scalar, self.unit)
        else:
            raise ValueError("Only scalar values can be multiplied using mul_scalar method, consider using * or mul_measurement.")
        
    def div_scalar(self, scalar: float | int) -> 'Measurement':
        """
        Divides the current measurement by a scalar value. **The unit of measurement remains UNCHANGED.**

        This method creates a new `Measurement` object with the result of dividing the current measurement's value by the scalar. **The unit of the measurement remains unchanged.**

        Args:
            scalar (float | int): The scalar value to divide the measurement by. Must be a number.

        Returns:
            Measurement: A new `Measurement` object with the updated value.

        Raises:
            ValueError: If the scalar is not a number.

        Example:
            >>> from ucalcx import Measurement, MetricPrefix
            >>> from ucalcx.length.imperial import Mile
            >>> two_miles = Measurement(2, Mile())
            >>> one_mile = two_miles.div_scalar(2)
            >>> print(one_mile) # Note that the unit is maintained i.e. still miles, not unitless
            1 mi
        """

        if isinstance(scalar, (int, float)):
            return Measurement(self.value / scalar, self.unit)
        else:
            raise ValueError("Only scalar values can be divided using div_scalar method, consider using / or div_measurement.")
    
    def __add__(self, other: 'Measurement') -> 'Measurement':
        """
        Adds another `Measurement` object to the current measurement using the `+` operator.

        This method performs addition between two `Measurement` objects by converting the other measurement to the unit of the current measurement. The result is a new `Measurement` object with the sum of the values.

        Args:
            other (Measurement): The `Measurement` object to add. Its unit must be compatible with the current measurement's unit.

        Returns:
            Measurement: A new `Measurement` object with the updated value.

        Raises:
            ValueError: If the units of the measurements are incompatible or if trying to add a scalar value.

        Example:
            >>> from ucalcx import Measurement, MetricPrefix
            >>> from ucalcx.length.metric import Meter
            >>> fifty_meters = Measurement(50, Meter())
            >>> one_kilometer = Measurement(1, Meter(MetricPrefix.Kilo))
            >>> new_length = fifty_meters + one_kilometer # Notice this does 50 + 1000, not 50 + 1
            >>> print(new_length) # Maintains the unit of the calling object
            1050 m
            >>> new_length = one_kilometer + fifty_meters # Notice this does 1 + 0.05, not 1 + 50
            >>> print(new_length) # Maintains the unit of the calling object
            1.05 km
        """

        if isinstance(other, (int, float)):
            raise ValueError("Trying to add a scalar to a Measurement. Use a Measurement object, so units are explicit. Otherwise, use add_scalar method.")

        if self.unit.quantity != other.unit.quantity:
            raise ValueError(f"Cannot add {self.unit.quantity.name} to {other.unit.quantity.name}.")
        
        converted_value = other.unit.convert_to(self.unit, other.value)
        return Measurement(self.value + converted_value, self.unit)
    
    def __sub__(self, other: 'Measurement') -> 'Measurement':
        """
        Subtracts another `Measurement` object from the current measurement using the `-` operator.

        This method performs subtraction between two `Measurement` objects by converting the other measurement to the unit of the current measurement. The result is a new `Measurement` object with the difference of the values.

        Args:
            other (Measurement): The `Measurement` object to subtract. Its unit must be compatible with the current measurement's unit.

        Returns:
            Measurement: A new `Measurement` object with the updated value.

        Raises:
            ValueError: If the units of the measurements are incompatible or if trying to subtract a scalar value.

        Example:
            >>> from ucalcx import Measurement, MetricPrefix
            >>> from ucalcx.length.metric import Meter
            >>> fifty_meters = Measurement(50, Meter())
            >>> one_kilometer = Measurement(1, Meter(MetricPrefix.Kilo))
            >>> new_length = one_kilometer - fifty_meters # Notice this does 1 - 0.05 1000, not 1000 - 1
            >>> print(new_length) # Maintains the unit of the calling object
            0.95 km
        """
        
        if isinstance(other, (int, float)):
            raise ValueError("Trying to subtract a scalar from a Measurement. Use a Measurement object, so units are explicit. Otherwise, use add_scalar method.")

        if self.unit.quantity != other.unit.quantity:
            raise ValueError(f"Cannot subtract {self.unit.quantity.name} from {other.unit.quantity.name}.")
        
        converted_value = other.unit.convert_to(self.unit, other.value)
        return Measurement(self.value - converted_value, self.unit)
    
    def __str__(self) -> str:
        return f"{self.value} {self.unit.full_symbol}"
