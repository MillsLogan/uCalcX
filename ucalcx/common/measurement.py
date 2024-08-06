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

        Example:
            >>> m = Measurement(5.0, length.metric.Meter())
            >>> print(m.value)
            5.0 # The value of the measurement in meters
            >>> new_measurement = m.convert_to(length.metric.Meter(MetricPrefix.Kilo))
            >>> print(new_measurement.value)
            0.005 # The value of the measurement in kilometers
            >>> print(new_measurement.unit)
            kilometer # The unit of the measurement
        """
        
        if other.quantity != self.unit.quantity:
            raise ValueError(f"Cannot convert {self.unit.quantity.name} to {other.quantity.name}.")
        
        converted_value = self.unit.convert_to(other, self.value)
        return Measurement(converted_value, other)
    
    def __str__(self) -> str:
        return f"{self.value} {self.unit.full_symbol}"
