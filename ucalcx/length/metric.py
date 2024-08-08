"""Module for Length Units in the Metric System.

This module contains classes for units of length in the metric system, 
including the base unit of the meter and its metric prefixes.

For more information about the metric system and its units, refer to the following resources:
- [Metric System on Wikipedia](https://en.wikipedia.org/wiki/Metric_system)
- [Meter on Wikipedia](https://en.wikipedia.org/wiki/Meter)

Example:
    To use the Meter class, simply import it and create an instance:

    >>> from ucalcx.length.metric import Meter
    >>> meter = Meter()
    >>> print(meter)
    meter (m)

    To create a kilometer unit, specify the MetricPrefix when creating the instance:

    >>> from ucalcx import MetricPrefix
    >>> from ucalcx.length.metric import Meter
    >>> kilometer = Meter(MetricPrefix.Kilo)
    >>> print(kilometer)
    kilometer (km)
"""


from .length_unit import LengthUnit
from ucalcx import MetricPrefix

class Meter(LengthUnit):
    """A concrete implementation of the `LengthUnit` class representing the meter unit of length.

    The Meter class represents the base unit of length in the metric system.
    It is equivalent to one meter and can be used to represent distances in meters
    without any metric prefixes applied. To represent larger or smaller distances,
    use the `MetricPrefix` enum to specify the desired metric prefix (e.g., `MetricPrefix.Kilo`
    for kilometers).

    Attributes:
        symbol (str): The symbol for the meter unit, 'm'.
        name (str): The name of the unit, "meter".
        meters_per_unit (float): The number of meters per unit (1.0 for the base meter unit).
    """

    symbol = 'm'
    name = "meter"
    meters_per_unit = 1.0
    
    
    def __init__(self, metric_prefix: 'MetricPrefix'=MetricPrefix.Base):
        """Initializes a new Meter instance with an optional metric prefix.

        Args:
            metric_prefix (MetricPrefix, optional): The metric prefix to apply to the meter unit. Defaults to `MetricPrefix.Base`.
        """
        
        super().__init__(metric_prefix)
