from ucalcx import Unit, Quantity, Unit, MetricPrefix


class TimeUnit(Unit):
    """
    Base class for time units.

    This class represents a time unit and provides methods to convert between the unit and the base unit of time (seconds).

    Attributes:
        name (str): The name of the time unit.
        symbol (str): The symbol for the time unit.
        seconds_per_unit (int): The number of seconds that this unit represents.

    Methods:
        convert(value: float, target_unit: TimeUnit) -> float:
            Converts a value from this time unit to another specified time unit.
    """

    def __init__(self, name: str, symbol: str, metric_prefix: 'MetricPrefix', seconds_per_unit: float) -> None:
        """
        Initializes a time unit with the given attributes.

        Args:
            name (str): The name of the time unit.
            symbol (str): The symbol for the time unit.
            seconds_per_unit (int): The number of seconds that this unit represents.
        """

        super().__init__(name, symbol, metric_prefix, Quantity.Time)
        self.seconds_per_unit = seconds_per_unit
        """ The conversion factor to seconds. I.e. 1 second = meters_per_unit * value """
        
    def convert_to(self, other: 'TimeUnit', value: float) -> float:
        
        if other.quantity != Quantity.Length:
            raise ValueError("Cannot convert between different quantities")


        this_to_other_factor: float = self.seconds_per_unit / other.seconds_per_unit
        converted_value: float = value * this_to_other_factor

        if other.metric_prefix != self.metric_prefix:
            converted_value = self.metric_prefix.convert_to(other.metric_prefix, converted_value)
        return converted_value        
