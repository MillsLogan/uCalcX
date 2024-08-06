"""
# length.imperial Module

The `length.imperial` module provides classes for units of length within the US Customary system. This module includes various length units used primarily in the United States, with support for applying metric prefixes. The default metric prefix for these units is `MetricPrefix.Base`.

All units in this module are subclasses of the `LengthUnit` class, which provides the base functionality for handling length units. Each unit has a specific conversion factor that defines how it relates to the base unit of meters, and allows use of metric prefixes.

## Available Units:
- **Foot**: Represents the foot unit of length.
- **Yard**: Represents the yard unit of length.
- **Mile**: Represents the mile unit of length.
- **Inch**: Represents the inch unit of length.
- **Thou (Mil)**: Represents a very small unit of length, commonly used in engineering and manufacturing.
- **Hand**: Represents the unit used to measure the height of horses.

## External Resources:
- [US Customary Units on Wikipedia](https://en.wikipedia.org/wiki/US_customary_units)
- [Foot on Wikipedia](https://en.wikipedia.org/wiki/Foot_(unit))
- [Yard on Wikipedia](https://en.wikipedia.org/wiki/Yard)
- [Mile on Wikipedia](https://en.wikipedia.org/wiki/Mile)
- [Inch on Wikipedia](https://en.wikipedia.org/wiki/Inch)
- [Thou (Mil) on Wikipedia](https://en.wikipedia.org/wiki/Thou_(unit))
- [Hand on Wikipedia](https://en.wikipedia.org/wiki/Hand_(unit))

The module is designed to facilitate conversions and calculations involving imperial units while allowing for optional metric prefix adjustments.
"""


from ucalcx.common import MetricPrefix
from .length_unit import LengthUnit        


class Inch(LengthUnit):
    """
    Represents the inch unit of length.

    The inch is a standard unit of length in the US Customary and British Imperial systems. 
    1 inch = 25.4 millimeters.

    Attributes:
        name (str): The name of the unit, which is always "inch".
        symbol (str): The symbol for the unit, which is always "in".
        conversion_factor (float): The conversion factor to convert from inch to meters (0.0254 meters).

    ## External Resource:
        [Inch on Wikipedia](https://en.wikipedia.org/wiki/Inch)
    """
    
    def __init__(self, metric_prefix: MetricPrefix = MetricPrefix.Base) -> None:
        """
        Initializes an Inch unit with a specified metric prefix.

        Args:
            metric_prefix (MetricPrefix, optional): The metric prefix to use. Defaults to `MetricPrefix.Base`.
        """
        
        super().__init__('inch', 'in', metric_prefix, 0.0254)
    
    
class Foot(LengthUnit):
    """
    Represents the foot unit of length.

    The foot is a standard unit of length in the US Customary and British Imperial systems.
    1 foot = 0.3048 meters.

    Attributes:
        name (str): The name of the unit, which is always "foot".
        symbol (str): The symbol for the unit, which is always "ft".
        conversion_factor (float): The conversion factor to convert from foot to meters (0.3048 meters).

    ## External Resource:
        [Foot on Wikipedia](https://en.wikipedia.org/wiki/Foot_(unit))
    """
    
    def __init__(self, metric_prefix: MetricPrefix = MetricPrefix.Base) -> None:
        """
        Initializes a Foot unit with a specified metric prefix.

        Args:
            metric_prefix (MetricPrefix, optional): The metric prefix to use. Defaults to `MetricPrefix.Base`.
        """
        
        super().__init__('foot', 'ft', metric_prefix, 0.3048)
        

class Yard(LengthUnit):
    """
    Represents the yard unit of length.

    The yard is a standard unit of length in the US Customary and British Imperial systems.
    1 yard = 0.9144 meters.

    Attributes:
        name (str): The name of the unit, which is always "yard".
        symbol (str): The symbol for the unit, which is always "yd".
        conversion_factor (float): The conversion factor to convert from yard to meters (0.9144 meters).

    ## External Resource:
        [Yard on Wikipedia](https://en.wikipedia.org/wiki/Yard)
    """
    
    def __init__(self, metric_prefix: MetricPrefix = MetricPrefix.Base) -> None:
        """
        Initializes a Yard unit with a specified metric prefix.

        Args:
            metric_prefix (MetricPrefix, optional): The metric prefix to use. Defaults to `MetricPrefix.Base`.
        """
        
        super().__init__('yard', 'yd', metric_prefix, 0.9144)
        

class Mile(LengthUnit):
    """
    Represents the mile unit of length.

    The mile is a standard unit of length in the US Customary and British Imperial systems.
    1 mile = 1609.344 meters.

    Attributes:
        name (str): The name of the unit, which is always "mile".
        symbol (str): The symbol for the unit, which is always "mi".
        conversion_factor (float): The conversion factor to convert from mile to meters (1609.344 meters).

    ## External Resource:
        [Mile on Wikipedia](https://en.wikipedia.org/wiki/Mile)
    """
    
    def __init__(self, metric_prefix: MetricPrefix = MetricPrefix.Base):
        """
        Initializes a Mile unit with a specified metric prefix.

        Args:
            metric_prefix (MetricPrefix, optional): The metric prefix to use. Defaults to `MetricPrefix.Base`.
        """
        
        super().__init__('mile', 'mi', metric_prefix, 1609.344)

class Thou(LengthUnit):
    """
    Represents the thou (or mil) unit of length.

    The thou (or mil) is a small unit of length commonly used in engineering and manufacturing.
    1 thou = 0.001 inches (0.0000254 meters).

    Attributes:
        name (str): The name of the unit, which is always "thou".
        symbol (str): The symbol for the unit, which is always "mil" or "thou".
        conversion_factor (float): The conversion factor to convert from thou to meters (0.0000254 meters).

    ## External Resource:
        [Thou (Mil) on Wikipedia](https://en.wikipedia.org/wiki/Thou_(unit))
    """

    def __init__(self, metric_prefix: MetricPrefix = MetricPrefix.Base):
        """
        Initializes a Thou unit with a specified metric prefix.

        Args:
            metric_prefix (MetricPrefix, optional): The metric prefix to use. Defaults to `MetricPrefix.Base`.
        """

        super().__init__(name='thou', symbol='mil', metric_prefix=metric_prefix, conversion_factor=0.0000254)

    
class Hand(LengthUnit):
    """
    Represents the hand unit of length.

    The hand is a unit of length traditionally used to measure the height of horses.
    1 hand = 4 inches (0.1016 meters).

    Attributes:
        name (str): The name of the unit, which is always "hand".
        symbol (str): The symbol for the unit, which is always "h".
        conversion_factor (float): The conversion factor to convert from hand to meters (0.1016 meters).

    ## External Resource:
        [Hand on Wikipedia](https://en.wikipedia.org/wiki/Hand_(unit))
    """

    def __init__(self, metric_prefix: MetricPrefix = MetricPrefix.Base):
        """
        Initializes a Hand unit with a specified metric prefix.

        Args:
            metric_prefix (MetricPrefix, optional): The metric prefix to use. Defaults to `MetricPrefix.Base`.
        """
        
        super().__init__(name='hand', symbol='h', metric_prefix=metric_prefix, conversion_factor=0.1016)

