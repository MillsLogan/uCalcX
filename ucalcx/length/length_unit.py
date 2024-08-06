from ucalcx import Unit, Quantity, Unit, MetricPrefix


class LengthUnit(Unit):
    """
    # LengthUnit Class

    Represents a unit of length. This class extends the `Unit` class and includes functionality for converting between different length units.

    Attributes:
        name (str): The name of the length unit.
        symbol (str): The symbol for the length unit.
        metric_prefix (MetricPrefix): The metric prefix associated with the length unit.
        conversion_factor (float): The conversion factor to convert this unit to meters.

    ## Methods:
        convert_to(self, other: LengthUnit, value: float) -> float:
            Converts the value from this length unit to another `LengthUnit`.
        
        _convert_to_meters(self, value: float) -> float:
            Converts the value from this unit to meters.

        _convert_from_meters(self, value: float) -> float:
            Converts the value from meters to this unit.

        

    Example:
        >>> length_unit = LengthUnit("meter", "m", MetricPrefixes.None_, 1.0)
        >>> length_in_kilometers = LengthUnit("kilometer", "km", MetricPrefixes.Kilo, 1000.0)
        >>> value_in_kilometers = length_unit.convert_to(length_in_kilometers, 5000.0)
        >>> print(value_in_kilometers)
        5.0
    """
    
    def __init__(self, name: str, symbol: str, metric_prefix: 'MetricPrefix', conversion_factor: float) -> None:
        """
        Initializes a new instance of the LengthUnit class.

        Args:
            name (str): The name of the length unit (e.g., "meter", "kilometer"). This is the descriptive term used to identify the unit.
            symbol (str): The symbol of the length unit (e.g., "m", "km"). This is the abbreviated representation used in calculations and measurements.
            metric_prefix (MetricPrefixes): The metric prefix associated with the length unit (e.g., `MetricPrefixes.Kilo` for kilo, `MetricPrefixes.Milli` for milli). This prefix is used to scale the unit and modify its magnitude.
            conversion_factor (float): The factor used to convert this length unit to meters. This value represents how many meters are equivalent to one unit of this length.
        """
        
        super().__init__(name, symbol, metric_prefix, Quantity.Length)
        self.conversion_factor = conversion_factor
        """ The conversion factor to meters. I.e. 1 meter = conversion_factor * value """
        
    def _convert_to_meters(self, value: float) -> float:
        """
        Converts the given length value from this unit to meters.

        Args:
            value (float): The length value in this unit.

        Returns:
            float: The length value in meters.
        """
        
        return value * self.conversion_factor
    
    def _convert_from_meters(self, value: float) -> float:
        """
        Converts a length value from meters to this unit.

        Args:
            value (float): The length value in meters.

        Returns:
            float: The length value in this unit.
        """
        
        return value / self.conversion_factor
        
    def convert_to(self, other: 'LengthUnit', value: float) -> float:
        """
        Converts the given length value from this unit to another `LengthUnit`.

        The method first converts the value to meters. It then checks if the metric prefixes of the units match, performs a conversion if they don't, and finally converts the value from meters to the target unit.

        Args:
            other (LengthUnit): The target length unit to convert to.
            value (float): The length value to convert.

        Returns:
            float: The converted length value in the target unit.
        """
        
        if other.quantity != Quantity.Length:
            raise ValueError("Cannot convert between different quantities")

        converted_value = self._convert_to_meters(value)
        if other.metric_prefix != self.metric_prefix:
            converted_value = self.metric_prefix.convert_to(other.metric_prefix, converted_value)
        return other._convert_from_meters(converted_value)        

