"""Module for Length Units in the Imperial or US Customary System.

This module provides classes for units of length in the imperial system,
including the base unit of the inch and other common imperial units like the foot, yard,
and mile, as well others.

Each imperial unit class defines conversions to the inch, which in turn has a conversion to the meter.

For more information about the imperial system and its units, refer to the following resources:
- [Imperial System on Wikipedia](https://en.wikipedia.org/wiki/Imperial_units)
- [Inch on Wikipedia](https://en.wikipedia.org/wiki/Inch)

Example:
    All units in this module can be imported and used individually. For example, to use the `Inch` class:

    >>> from ucalcx.length.imperial import Inch
    >>> inch = Inch()
    >>> print(inch)
    inch (in)
"""


from ucalcx.common import MetricPrefix
from .length_unit import LengthUnit        


class ImperialLengthUnit(LengthUnit):
    """A base class for units of length in the Imperial or US Customary System.

    This class extends the `LengthUnit` class and provides a common base for all imperial length units.
    Most imperial units are defined in terms of each other, so for conversions, they are first converted
    to inches and then to meters. This class assumes that the child classes define the `inches_per_unit`
    attribute to specify the number of inches per unit. The `meters_per_unit` attribute is also defined
    here as a default value for the conversion to meters. See the `Foot` class for a concrete example
    of an imperial length unit.

    Attributes:
        inches_per_unit (float): The number of inches per unit of the imperial length.
        metric_prefix (MetricPrefix): The metric prefix to apply to the imperial unit. Defaults to `MetricPrefix.Base`.

        meters_per_unit (float): The number of meters per unit of the imperial length. Defaults to 0.0254.
    """

    inches_per_unit: float
    metric_prefix: MetricPrefix = MetricPrefix.Base
    meters_per_unit: float = 0.0254 # Also defined in Inch class just for reference

    def __init__(self, *_) -> None:
        """Initializes a new ImperialLengthUnit instance, takes an argument to conform to the `LengthUnit` class"""

        super().__init__(self.metric_prefix)


    def convert_to(self, other: LengthUnit, value: float) -> float:
        """Converts the given value from this imperial unit to another length unit.
        
        This method first converts the value to inches and then to the target unit. Using meters as an intermediary.

        Args:
            other (LengthUnit): The target length unit to convert the value to.
            value (float): The value to convert.

        Returns:
            float: The converted value in the target length unit.

        Raises:
            ValueError: If the target unit is not a valid length unit.
        """

        if isinstance(other, ImperialLengthUnit):
            return value * (self.inches_per_unit / other.inches_per_unit)
        return super().convert_to(other, self.convert_to(Inch(), value))


class Thou(ImperialLengthUnit):
    """A unit of length equal to one thousandth of an inch, commonly used in the imperial system.

    - **Name**: "thou"
    - **Symbol**: "mil"
    - **Inches per Unit**: 0.001

    More information about the thou can be found in the following resource:
    - [Thou on Wikipedia](https://en.wikipedia.org/wiki/Thou)
    """

    name: str = "thou"
    symbol: str = "mil"
    inches_per_unit: float = 0.001


class Inch(ImperialLengthUnit):
    """A unit of length equal to one inch, commonly used in the imperial system.

    This class is used as the base unit for the imperial length system, with other units defined in terms of inches.
    
    - **Name**: "inch"
    - **Symbol**: "in"
    - **Inches per Unit**: 1
    - **Meters per Unit**: 0.0254

    More information about the inch can be found in the following resource:
    - [Inch on Wikipedia](https://en.wikipedia.org/wiki/Inch)
    """

    name: str = "inch"
    symbol: str = "in"
    inches_per_unit: float = 1.0
    meters_per_unit: float = 0.0254 # Also defined in ImperialLengthUnit class just for reference
    

class Hand(ImperialLengthUnit):
    """A unit of length equal to one quarter of a foot, commonly used in the imperial system for measuring horse height.

    - **Name**: "hand"
    - **Symbol**: "hh"
    - **Inches per Unit**: 4

    More information about the hand can be found in the following resource:
    - [Hand (unit) on Wikipedia](https://en.wikipedia.org/wiki/Hand_(unit))
    """

    name: str = "hand"
    symbol: str = "hh"
    inches_per_unit: float = 4.0


class Foot(ImperialLengthUnit):
    """A unit of length equal to twelve inches, commonly used in the imperial system.

    - **Name**: "foot"
    - **Symbol**: "ft"
    - **Inches per Unit**: 12

    More information about the foot can be found in the following resource:
    - [Foot on Wikipedia](https://en.wikipedia.org/wiki/Foot_(unit))
    """

    name: str = "foot"
    symbol: str = "ft"
    inches_per_unit: float = 12.0
        

class Yard(ImperialLengthUnit):
    """A unit of length equal to three feet, commonly used in the imperial system for measuring longer distances.

    - **Name**: "yard"
    - **Symbol**: "yd"
    - **Inches per Unit**: 36

    More information about the yard can be found in the following resource:
    - [Yard on Wikipedia](https://en.wikipedia.org/wiki/Yard_(unit))
    """

    name: str = "yard"
    symbol: str = "yd"
    inches_per_unit: float = 36.0        


class Mile(ImperialLengthUnit):
    """A unit of length equal to 5,280 feet, commonly used in the imperial system for measuring long distances.

    - **Name**: "mile"
    - **Symbol**: "mi"
    - **Feet per Unit**: 5280

    More information about the mile can be found in the following resource:
    - [Mile on Wikipedia](https://en.wikipedia.org/wiki/Mile)
    """

    name: str = "mile"
    symbol: str = "mi"
    inches_per_unit: float = 63360.0


