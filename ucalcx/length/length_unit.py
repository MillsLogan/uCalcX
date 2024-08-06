from ucalcx import Unit, Quantity, Unit, MetricPrefix


class LengthUnit(Unit):
    """
    # LengthUnit Class

    Represents a unit of length. This class extends the `Unit` class and includes functionality for converting between different length units.

    Attributes:
        name (str): The name of the length unit.
        symbol (str): The symbol for the length unit.
        metric_prefix (MetricPrefix): The metric prefix associated with the length unit.
        meters_per_unit (float): The conversion factor to convert this unit to meters.

    ## Methods:
        convert_to(self, other: LengthUnit, value: float) -> float:
            Converts the value from this length unit to another `LengthUnit`.

    Example:
        >>> length_unit = LengthUnit("meter", "m", MetricPrefixes.None_, 1.0)
        >>> length_in_kilometers = LengthUnit("kilometer", "km", MetricPrefixes.Kilo, 1000.0)
        >>> value_in_kilometers = length_unit.convert_to(length_in_kilometers, 5000.0)
        >>> print(value_in_kilometers)
        5.0
    """
    
    def __init__(self, name: str, symbol: str, metric_prefix: 'MetricPrefix', meters_per_unit: float) -> None:
        """
        Initializes a new instance of the LengthUnit class.

        Args:
            name (str): The name of the length unit (e.g., "meter", "kilometer"). This is the descriptive term used to identify the unit.
            symbol (str): The symbol of the length unit (e.g., "m", "km"). This is the abbreviated representation used in calculations and measurements.
            metric_prefix (MetricPrefixes): The metric prefix associated with the length unit (e.g., `MetricPrefixes.Kilo` for kilo, `MetricPrefixes.Milli` for milli). This prefix is used to scale the unit and modify its magnitude.
            meters_per_unit (float): The factor used to convert this length unit to meters. This value represents how many meters are equivalent to one unit of this length.
        """
        
        super().__init__(name, symbol, metric_prefix, Quantity.Length)
        self.meters_per_unit = meters_per_unit
        """ How many meters are equivalent to one unit of this length """
        
    def convert_to(self, other: 'LengthUnit', value: float) -> float:
        """
        Converts the given length value from this unit to another `LengthUnit`.

        The method converts the given length value from this unit to another `LengthUnit` using the meter as an intermediate unit.

        Args:
            other (LengthUnit): The target length unit to convert to.
            value (float): The length value to convert.

        Returns:
            float: The converted length value in the target unit.
        """
        
        if other.quantity != Quantity.Length:
            raise ValueError("Cannot convert between different quantities")

        this_to_other_factor: float = self.meters_per_unit / other.meters_per_unit
        converted_value: float = value * this_to_other_factor
        if other.metric_prefix != self.metric_prefix:
            converted_value = self.metric_prefix.convert_to(other.metric_prefix, converted_value)
        return converted_value        

