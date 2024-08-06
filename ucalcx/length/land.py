"""
# length.land Module

The `length.land` module provides classes for units of length used in land measurement and surveying. This module includes various units traditionally used in land measurement, with support for applying metric prefixes. The default metric prefix for these units is `MetricPrefix.Base`.

This module extends `LengthUnit` and supports metric prefixes.

## Available Units:
- **Rod**: Represents the rod unit of length, traditionally used in land measurement.
- **Chain**: Represents the chain unit of length, used in surveying and land measurement.
- **Furlong**: Represents the furlong unit of length, historically used in horse racing and land measurement.

## External Resources:
- [Rod on Wikipedia](https://en.wikipedia.org/wiki/Rod_(unit))
- [Chain on Wikipedia](https://en.wikipedia.org/wiki/Chain_(unit))
- [Furlong on Wikipedia](https://en.wikipedia.org/wiki/Furlong)

The module is designed to facilitate conversions and calculations involving land measurement units while allowing for optional metric prefix adjustments. Additional units related to land measurement can be added as needed.
"""

from .length_unit import LengthUnit
from ucalcx import MetricPrefix

class Rod(LengthUnit):
    """
    Represents the rod unit of length.

    The rod is a unit of length used in land measurement and surveying.
    1 rod = 5.0292 meters.

    Attributes:
        name (str): The name of the unit, which is always "rod".
        symbol (str): The symbol for the unit, which is always "rd".
        conversion_factor (float): The conversion factor to convert from rod to meters (5.0292 meters).

    ## External Resource:
        [Rod on Wikipedia](https://en.wikipedia.org/wiki/Rod_(unit))
    """

    def __init__(self, metric_prefix: MetricPrefix = MetricPrefix.Base) -> None:
        """
        Initializes a Rod unit with a specified metric prefix.

        Args:
            metric_prefix (MetricPrefix, optional): The metric prefix to use. Defaults to `MetricPrefix.Base`.
        """

        super().__init__(name='rod', symbol='rd', metric_prefix=metric_prefix, conversion_factor=5.0292)


class Chain(LengthUnit):
    """
    Represents the chain unit of length.

    The chain is a unit of length used in surveying and land measurement.
    1 chain = 20.1168 meters.

    Attributes:
        name (str): The name of the unit, which is always "chain".
        symbol (str): The symbol for the unit, which is always "ch".
        conversion_factor (float): The conversion factor to convert from chain to meters (20.1168 meters).

    ## External Resource:
        [Chain on Wikipedia](https://en.wikipedia.org/wiki/Chain_(unit))
    """

    def __init__(self, metric_prefix: MetricPrefix = MetricPrefix.Base) -> None:
        """
        Initializes a Chain unit with a specified metric prefix.

        Args:
            metric_prefix (MetricPrefix, optional): The metric prefix to use. Defaults to `MetricPrefix.Base`.
        """

        super().__init__(name='chain', symbol='ch', metric_prefix=metric_prefix, conversion_factor=20.1168)


class Furlong(LengthUnit):
    """
    Represents the furlong unit of length.

    The furlong is a unit of length historically used in horse racing and land measurement.
    1 furlong = 201.168 meters.

    Attributes:
        name (str): The name of the unit, which is always "furlong".
        symbol (str): The symbol for the unit, which is always "fur".
        conversion_factor (float): The conversion factor to convert from furlong to meters (201.168 meters).

    ## External Resource:
        [Furlong on Wikipedia](https://en.wikipedia.org/wiki/Furlong)
    """

    def __init__(self, metric_prefix: MetricPrefix = MetricPrefix.Base):
        """
        Initializes a Furlong unit with a specified metric prefix.

        Args:
            metric_prefix (MetricPrefix, optional): The metric prefix to use. Defaults to `MetricPrefix.Base`.
        """

        super().__init__(name='furlong', symbol='fur', metric_prefix=metric_prefix, conversion_factor=201.168)
