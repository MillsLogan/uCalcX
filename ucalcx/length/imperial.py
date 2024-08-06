"""
# length.imperial Module

The `length.imperial` module provides classes for units of length within the US Customary system. This module includes various length units used primarily in the United States, with support for applying metric prefixes. The default metric prefix for these units is `MetricPrefix.Base`.

This module extends `LengthUnit` and supports metric prefixes.

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
    Represents the inch unit of length, commonly used in the imperial system.

    - **Name**: "inch"
    - **Symbol**: "in"
    - **Meters per Unit**: 0.0254

    Args:
        metric_prefix (MetricPrefix): The metric prefix to apply to the inch unit. Defaults to `MetricPrefix.Base`.

    For more information about the inch and its usage, refer to the following resource:
    - [Inch on Wikipedia](https://en.wikipedia.org/wiki/Inch)
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
    Represents the foot unit of length, commonly used in the imperial system.

    - **Name**: "foot"
    - **Symbol**: "ft"
    - **Meters per Unit**: 0.3048

    Args:
        metric_prefix (MetricPrefix): The metric prefix to apply to the foot unit. Defaults to `MetricPrefix.Base`.

    For more information about the foot and its usage, refer to the following resource:
    - [Foot on Wikipedia](https://en.wikipedia.org/wiki/Foot_(unit))
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
    Represents the yard unit of length, commonly used in the imperial system.

    - **Name**: "yard"
    - **Symbol**: "yd"
    - **Meters per Unit**: 0.9144

    Args:
        metric_prefix (MetricPrefix): The metric prefix to apply to the yard unit. Defaults to `MetricPrefix.Base`.

    For more information about the yard and its usage, refer to the following resource:
    - [Yard on Wikipedia](https://en.wikipedia.org/wiki/Yard)
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
    Represents the mile unit of length, commonly used in the imperial system.

    - **Name**: "mile"
    - **Symbol**: "mi"
    - **Meters per Unit**: 1609.34

    Args:
        metric_prefix (MetricPrefix): The metric prefix to apply to the mile unit. Defaults to `MetricPrefix.Base`.

    For more information about the mile and its usage, refer to the following resource:
    - [Mile on Wikipedia](https://en.wikipedia.org/wiki/Mile)
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
    Represents the thou (mil) unit of length, commonly used in engineering and manufacturing within the imperial system.

    - **Name**: "thou"
    - **Symbol**: "thou"
    - **Meters per Unit**: 0.0000254

    Args:
        metric_prefix (MetricPrefix): The metric prefix to apply to the thou unit. Defaults to `MetricPrefix.Base`.

    For more information about the thou and its usage, refer to the following resource:
    - [Thou on Wikipedia](https://en.wikipedia.org/wiki/Thou_(unit))
    """

    def __init__(self, metric_prefix: MetricPrefix = MetricPrefix.Base):
        """
        Initializes a Thou unit with a specified metric prefix.

        Args:
            metric_prefix (MetricPrefix, optional): The metric prefix to use. Defaults to `MetricPrefix.Base`.
        """

        super().__init__(name='thou', symbol='mil', metric_prefix=metric_prefix, meters_per_unit=0.0000254)

    
class Hand(LengthUnit):
    """
    Represents the hand unit of length, commonly used to measure the height of horses within the imperial system.

    - **Name**: "hand"
    - **Symbol**: "hh"
    - **Meters per Unit**: 0.1016

    Args:
        metric_prefix (MetricPrefix): The metric prefix to apply to the hand unit. Defaults to `MetricPrefix.Base`.

    For more information about the hand and its usage, refer to the following resource:
    - [Hand on Wikipedia](https://en.wikipedia.org/wiki/Hand_(unit))
    """


    def __init__(self, metric_prefix: MetricPrefix = MetricPrefix.Base):
        """
        Initializes a Hand unit with a specified metric prefix.

        Args:
            metric_prefix (MetricPrefix, optional): The metric prefix to use. Defaults to `MetricPrefix.Base`.
        """
        
        super().__init__(name='hand', symbol='h', metric_prefix=metric_prefix, meters_per_unit=0.1016)

