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
    Represents the rod unit of length, commonly used in land measurement.

    - **Name**: "rod"
    - **Symbol**: "rd"
    - **Meters per Unit**: 5.0292

    Args:
        metric_prefix (MetricPrefix): The metric prefix to apply to the rod unit. Defaults to `MetricPrefix.Base`.

    For more information about the rod and its usage, refer to the following resource:
    - [Rod on Wikipedia](https://en.wikipedia.org/wiki/Rod_(unit))
    """

    name: str = "rod"
    symbol: str = "rd"
    meters_per_unit: float = 5.0292

    def __init__(self, metric_prefix: MetricPrefix = MetricPrefix.Base) -> None:
        """
        Initializes a Rod unit with a specified metric prefix.

        Args:
            metric_prefix (MetricPrefix, optional): The metric prefix to use. Defaults to `MetricPrefix.Base`.
        """

        super().__init__(metric_prefix)

class Chain(LengthUnit):
    """
    Represents the chain unit of length, commonly used in land measurement.

    - **Name**: "chain"
    - **Symbol**: "ch"
    - **Meters per Unit**: 20.1168

    Args:
        metric_prefix (MetricPrefix): The metric prefix to apply to the chain unit. Defaults to `MetricPrefix.Base`.

    For more information about the chain and its usage, refer to the following resource:
    - [Chain on Wikipedia](https://en.wikipedia.org/wiki/Chain_(unit))
    """

    name: str = "chain"
    symbol: str = "ch"
    meters_per_unit: float = 20.1168

    def __init__(self, metric_prefix: MetricPrefix = MetricPrefix.Base) -> None:
        """
        Initializes a Chain unit with a specified metric prefix.

        Args:
            metric_prefix (MetricPrefix, optional): The metric prefix to use. Defaults to `MetricPrefix.Base`.
        """

        super().__init__(metric_prefix)


class Furlong(LengthUnit):
    """
    Represents the furlong unit of length, commonly used in land measurement.

    - **Name**: "furlong"
    - **Symbol**: "fur"
    - **Meters per Unit**: 201.168

    Args:
        metric_prefix (MetricPrefix): The metric prefix to apply to the furlong unit. Defaults to `MetricPrefix.Base`.

    For more information about the furlong and its usage, refer to the following resource:
    - [Furlong on Wikipedia](https://en.wikipedia.org/wiki/Furlong)
    """

    name: str = "furlong"
    symbol: str = "fur"
    meters_per_unit: float = 201.168

    def __init__(self, metric_prefix: MetricPrefix = MetricPrefix.Base):
        """
        Initializes a Furlong unit with a specified metric prefix.

        Args:
            metric_prefix (MetricPrefix, optional): The metric prefix to use. Defaults to `MetricPrefix.Base`.
        """

        super().__init__(metric_prefix)
