"""
# metric Module

The `metric` module provides classes for units of length within the metric system. It includes the `Meter` class, which represents the meter unit with the ability to apply different metric prefixes.

## Meter Class:
    The `Meter` class extends the `LengthUnit` class to define the meter unit of length. It is initialized with a specific metric prefix, allowing for convenient creation of length units like kilometers, centimeters, etc., based on the meter unit.

    Attributes:
        name (str): The name of the unit, which is always "meter".
        symbol (str): The symbol for the unit, which is always "m".
        metric_prefix (MetricPrefixes): The metric prefix associated with the meter unit (e.g., `MetricPrefix.Kilo` for kilometers). Defaults to `MetricPrefix.Base` for the base meter unit.

    Example:
        >>> from ucalcx.length.metric import Meter
        >>> kilometer = Meter(MetricPrefix.Kilo)
        >>> print(kilometer.full_name)
        KiloMeter
        >>> print(kilometer.symbol)
        km
"""

from .length_unit import LengthUnit
from ucalcx import MetricPrefix

class Meter(LengthUnit):
    """
    # Meter Class

    Represents the meter unit of length, the base unit in the metric system. This class extends `LengthUnit` to provide a specific implementation of the meter unit with various metric prefixes.

    - **Name**: "meter"
    - **Symbol**: "m"
    - **Conversion Factor**: 1.0 (as it represents the base meter unit)

    Args:
        metric_prefix (MetricPrefix): The metric prefix to apply to the meter unit (e.g., `MetricPrefix.Kilo` for kilometers).

    For more information about the meter and its usage, refer to the following resource:
    - [Meter on Wikipedia](https://en.wikipedia.org/wiki/Meter)

    Example:
        >>> from ucalcx.length.metric import Meter
        >>> kilometer = Meter(MetricPrefix.Kilo)
        >>> print(kilometer.full_name)
        kilometer
        >>> print(kilometer.symbol)
        km
        >>> print(kilometer.conversion_factor)
        1.0 # Note that the conversion factor is still 1.0, however, the value will be adjusted based on the metric prefix.
        # This is handled internally when using the `convert_to` method, but outside callers should be aware of this.
    """
    
    def __init__(self, metric_prefix: 'MetricPrefix'=MetricPrefix.Base):
        """
        Initializes a new instance of the Meter class.

        Args:
            metric_prefix (MetricPrefix): The metric prefix to apply to the meter unit (e.g., `MetricPrefix.Kilo` for kilometers).

        Sets the unit name to "meter", the symbol to "m", and the conversion factor to 1.0, representing the base meter unit.
        """
        
        super().__init__('meter', 'm', metric_prefix, 1)