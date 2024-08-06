"""
# length.metric Module

The `metric` module provides classes for units of length within the metric system. This class extends `LengthUnit` and supports metric prefixes.

Available Units:
- **Meter**: Represents the meter unit of length, the base unit in the metric system.

Example:
    >>> from ucalcx.length.metric import Meter
    >>> kilometer = Meter(MetricPrefix.Kilo)
    >>> print(kilometer.full_name)
    kilometer
    >>> print(kilometer.symbol)
    km
    >>> print(kilometer.meters_per_unit)
    1.0
"""


from .length_unit import LengthUnit
from ucalcx import MetricPrefix

class Meter(LengthUnit):
    """
    Represents the meter unit of length, the base unit in the metric system.

    - **Name**: "meter"
    - **Symbol**: "m"
    - **Meters per Unit**: 1.0 (as it represents the base unit of length)

    Args:
        metric_prefix (MetricPrefix): The metric prefix to apply to the meter unit (e.g., `MetricPrefix.Kilo` for kilometers).

    For more information about the meter and its usage, refer to the following resource:
    - [Meter on Wikipedia](https://en.wikipedia.org/wiki/Meter)
    """
    
    def __init__(self, metric_prefix: 'MetricPrefix'=MetricPrefix.Base):
        """
        Initializes a new instance of the Meter class.

        Args:
            metric_prefix (MetricPrefix): The metric prefix to apply to the meter unit (e.g., `MetricPrefix.Kilo` for kilometers).

        Sets the unit name to "meter", the symbol to "m", and the conversion factor to 1.0, representing the base meter unit.
        """
        
        super().__init__('meter', 'm', metric_prefix, 1)