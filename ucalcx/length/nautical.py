"""
# length.nautical Module

The `length.nautical` module provides classes for units of length used primarily in maritime and navigation contexts. This module includes various units that are standard in nautical measurements, with support for applying metric prefixes. The default metric prefix for these units is `MetricPrefix.Base`.

This module extends `LengthUnit` and supports metric prefixes.

## Available Units:
- **Fathom**: Represents the fathom unit of length, commonly used to measure water depth.
- **Nautical Mile**: Represents the nautical mile unit of length, used in navigation and aviation, based on the Earth's circumference.
- **Cable**: Represents the cable unit of length, used in maritime contexts to measure distance at sea.

## External Resources:
- [Fathom on Wikipedia](https://en.wikipedia.org/wiki/Fathom)
- [Nautical Mile on Wikipedia](https://en.wikipedia.org/wiki/Nautical_mile)
- [Cable (Nautical) on Wikipedia](https://en.wikipedia.org/wiki/Cable_(unit))

The module is designed to facilitate conversions and calculations involving nautical units while allowing for optional metric prefix adjustments. Additional units related to nautical measurements can be added as needed.
"""

from .length_unit import LengthUnit
from ucalcx import MetricPrefix

      
class NauticalMile(LengthUnit):
    """
    Represents the nautical mile unit of length, commonly used in maritime and aviation contexts.

    - **Name**: "nautical mile"
    - **Symbol**: "NM"
    - **Meters per Unit**: 1852.0

    Args:
        metric_prefix (MetricPrefix): The metric prefix to apply to the nautical mile unit. Defaults to `MetricPrefix.Base`.

    For more information about the nautical mile and its usage, refer to the following resource:
    - [Nautical Mile on Wikipedia](https://en.wikipedia.org/wiki/Nautical_mile)
    """

    def __init__(self, metric_prefix: MetricPrefix = MetricPrefix.Base) -> None:
        """
        Initializes a Nautical Mile unit with a specified metric prefix.

        Args:
            metric_prefix (MetricPrefix, optional): The metric prefix to use. Defaults to `MetricPrefix.Base`.
        """

        super().__init__('nautical mile', 'nmi', metric_prefix, 1852)
        
        
class Fathom(LengthUnit):
    """
    Represents the fathom unit of length, commonly used in nautical contexts.

    - **Name**: "fathom"
    - **Symbol**: "ftm"
    - **Meters per Unit**: 1.8288

    Args:
        metric_prefix (MetricPrefix): The metric prefix to apply to the fathom unit. Defaults to `MetricPrefix.Base`.

    For more information about the fathom and its usage, refer to the following resource:
    - [Fathom on Wikipedia](https://en.wikipedia.org/wiki/Fathom)
    """

    def __init__(self, metric_prefix: MetricPrefix = MetricPrefix.Base) -> None:
        """
        Initializes a Fathom unit with a specified metric prefix.

        Args:
            metric_prefix (MetricPrefix, optional): The metric prefix to use. Defaults to `MetricPrefix.Base`.
        """
        
        super().__init__('fathom', 'ftm', metric_prefix, 1.8288)
        
    
class Cable(LengthUnit):
    """
    Represents the cable unit of length, commonly used in nautical contexts.

    - **Name**: "cable"
    - **Symbol**: "cable"
    - **Meters per Unit**: 185.2

    Args:
        metric_prefix (MetricPrefix): The metric prefix to apply to the cable unit. Defaults to `MetricPrefix.Base`.

    For more information about the cable and its usage, refer to the following resource:
    - [Cable on Wikipedia](https://en.wikipedia.org/wiki/Cable_length)
    """
    
    def __init__(self, metric_prefix: MetricPrefix = MetricPrefix.Base) -> None:
        """
        Initializes a Cable unit with a specified metric prefix.

        Args:
            metric_prefix (MetricPrefix, optional): The metric prefix to use. Defaults to `MetricPrefix.Base`.
        """
        
        super().__init__('cable', 'cbl', metric_prefix, 185.2)