from ucalcx import Unit, Quantity, Unit, MetricPrefix


class TimeUnit(Unit):
    """
    Base class for time units.

    This class represents a time unit and provides methods to convert between the unit and the base unit of time (seconds).

    Attributes:
        name (str): The name of the time unit.
        symbol (str): The symbol for the time unit.
        seconds_per_unit (int): The number of seconds that this unit represents.

    ## Methods:
        convert(value: float, target_unit: TimeUnit) -> float:
            Converts a value from this time unit to another specified time unit.
    """

    name: str
    symbol: str
    seconds_per_unit: float
    quantity: Quantity = Quantity.Time

    def __init__(self, metric_prefix: MetricPrefix) -> None:
        """
        Initializes a time unit with the given attributes.

        Args:
            name (str): The name of the time unit.
            symbol (str): The symbol for the time unit.
            seconds_per_unit (int): The number of seconds that this unit represents.
        """

        super().__init__(metric_prefix)
        """ The conversion factor to seconds. I.e. 1 second = meters_per_unit * value """
        
    def convert_to(self, other: 'TimeUnit', value: float) -> float:
        """
        Converts a value from this time unit to another time unit.

        This method converts the given value to the target time unit by first converting the value to seconds (the base unit of time) and then converting from seconds to the target unit. It also accounts for any differences in metric prefixes.

        Args:
            other (TimeUnit): The target time unit to convert to.
            value (float): The value in the current time unit to be converted.

        Returns:
            float: The converted value in the target time unit.

        Raises:
            ValueError: If the `other` unit does not have the same quantity as this unit.

        Example:
            >>> from ucalcx.time import Second, Minute
            >>> second = Second()
            >>> minute = Minute()
            >>> result = second.convert_to(minute, 120)  # Converts 120 seconds to minutes
            >>> print(result)
            2.0

        For more information about time unit conversions, refer to the following resource:
        - [Time on Wikipedia](https://en.wikipedia.org/wiki/Time)
        """

        if other.quantity != Quantity.Time:
            raise ValueError("Cannot convert between different quantities")


        this_to_other_factor: float = self.seconds_per_unit / other.seconds_per_unit
        converted_value: float = value * this_to_other_factor

        if other.metric_prefix != self.metric_prefix:
            converted_value = self.metric_prefix.convert_to(other.metric_prefix, converted_value)
        return converted_value        
