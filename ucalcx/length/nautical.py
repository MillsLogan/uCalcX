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
    Represents the nautical mile unit of length.

    The nautical mile is a unit of length used in navigation and aviation, based on the Earth's circumference.
    1 nautical mile = 1852 meters.

    Attributes:
        name (str): The name of the unit, which is always "nautical mile".
        symbol (str): The symbol for the unit, which is always "nmi".
        conversion_factor (float): The conversion factor to convert from nautical mile to meters (1852 meters).

    ## External Resource:
        [Nautical Mile on Wikipedia](https://en.wikipedia.org/wiki/Nautical_mile)
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
    Represents the fathom unit of length.

    The fathom is a unit of length used primarily to measure water depth in nautical contexts.
    1 fathom = 1.8288 meters.

    Attributes:
        name (str): The name of the unit, which is always "fathom".
        symbol (str): The symbol for the unit, which is always "ftm".
        conversion_factor (float): The conversion factor to convert from fathom to meters (1.8288 meters).

    ## External Resource:
        [Fathom on Wikipedia](https://en.wikipedia.org/wiki/Fathom)
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
    Represents the cable unit of length.

    The cable is a unit of length used in maritime contexts to measure distance at sea.
    1 cable = 185.2 meters.

    Attributes:
        name (str): The name of the unit, which is always "cable".
        symbol (str): The symbol for the unit, which is always "cbl".
        conversion_factor (float): The conversion factor to convert from cable to meters (185.2 meters).

    ## External Resource:
        [Cable (Nautical) on Wikipedia](https://en.wikipedia.org/wiki/Cable_(unit))
    """
    
    def __init__(self, metric_prefix: MetricPrefix = MetricPrefix.Base) -> None:
        """
        Initializes a Cable unit with a specified metric prefix.

        Args:
            metric_prefix (MetricPrefix, optional): The metric prefix to use. Defaults to `MetricPrefix.Base`.
        """
        
        super().__init__('cable', 'cbl', metric_prefix, 185.2)