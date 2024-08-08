from ucalcx import Unit, Quantity, Unit, MetricPrefix


class LengthUnit(Unit):
    """LengthUnit class for representing units of length.
    
    This class provides a base class for defining units of length. It extends the `Unit` class
    and adds additional properties specific to length units, such as the quantity of length.
    and requires the `meters_per_unit` attribute to be defined in the derived classes.
    
    Attributes:
        name (str): The name of the length unit (e.g., "meter", "kilometer"). This is the descriptive term used to identify the unit.
        symbol (str): The symbol of the length unit (e.g., "m", "km"). This is the abbreviated representation used in calculations and measurements.
        meters_per_unit (float): The factor used to convert this length unit to meters. This value represents how many meters are equivalent to one unit of this length.
        quantity (Quantity): The quantity of length that this unit represents. Defaults to `Quantity.Length`.
    """

    name: str
    symbol: str
    meters_per_unit: float
    quantity: Quantity = Quantity.Length
    
    def __init__(self, metric_prefix: 'MetricPrefix') -> None:
        """
        Initializes a new instance of the LengthUnit class.

        Args:
            metric_prefix (MetricPrefix): The metric prefix to apply to the length unit.
        """
        
        super().__init__(metric_prefix) 
        
    def convert_to(self, other: 'LengthUnit', value: float) -> float:
        """Converts the given length value from this unit to another `LengthUnit`.

        The method converts the given length value from this unit to another `LengthUnit` 
        using the meter as an intermediate unit.

        Args:
            other (LengthUnit): The target length unit to convert to.
            value (float): The length value to convert.

        Returns:
            float: The converted length value in the target unit.

        Raises:
            ValueError: If the target unit is not a length unit.
        """
        
        if other.quantity != Quantity.Length:
            raise ValueError("Cannot convert between different quantities")

        this_to_other_factor: float = self.meters_per_unit / other.meters_per_unit
        converted_value: float = value * this_to_other_factor
        if other.metric_prefix != self.metric_prefix:
            converted_value = self.metric_prefix.convert_to(other.metric_prefix, converted_value)
        return converted_value        

