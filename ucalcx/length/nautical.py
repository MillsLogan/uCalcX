"""Module for length units commonly used in nautical and maritime contexts.

This module contains classes for units of length used in nautical and maritime contexts,
including the nautical mile, cable, and fathom. These units are used to measure distances
at sea and are part of the nautical system of measurement.

The Fathom class is a subclass of the ImperialLengthUnit class, which provides a common
interface for working with imperial length units. The NauticalMile and Cable classes are
subclasses of the LengthUnit class, which provides a common interface for working with
units of length. None of these classes take a metric prefix as an argument, as they are
typically used in their base form.

For more information about nautical units and their history, refer to the following resources:
- [Nautical Mile on Wikipedia](https://en.wikipedia.org/wiki/Nautical_mile)
- [Fathom on Wikipedia](https://en.wikipedia.org/wiki/Fathom)
- [Cable on Wikipedia](https://en.wikipedia.org/wiki/Cable_(unit))

Example:
    All units in this module can be imported and used individually. For example, to use the `NauticalMile` class:

    >>> from ucalcx.length.nautical import NauticalMile
    >>> nautical_mile = NauticalMile()
    >>> print(nautical_mile)
    nautical_mile (NM) # Note the underscore in the name
"""

from ucalcx.common import MetricPrefix
from .imperial import ImperialLengthUnit        
from .length_unit import LengthUnit


class NauticalMile(LengthUnit):
    """A class representing the nautical mile unit of length.

    The nautical mile is a unit of length used in maritime and navigation contexts.
    It is equal to 1852 meters or 6076.1155 feet.

    - **Name**: "nautical_mile"
    - **Symbol**: "NM"
    - **Meters per Unit**: 1852.0

    More information about the nautical mile unit can be found in the following resource:
    - [Nautical Mile on Wikipedia](https://en.wikipedia.org/wiki/Nautical_mile)
    """

    name: str = "nautical_mile"
    symbol: str = "NM"
    meters_per_unit: float = 1852.0
    metric_prefix: MetricPrefix = MetricPrefix.Base

    def __init__(self, *_) -> None:
        """Initializes a new NauticalMile instance, takes an argument to conform to the `LengthUnit` class
        
        Takes an unused argument to conform to the `LengthUnit` class.
        """

        # Must take metric prefix as an argument to conform to the LengthUnit class
        super().__init__(self.metric_prefix)


class Cable(LengthUnit):
    """A class representing the cable unit of length.

    The cable is a unit of length used in maritime and navigation contexts.
    It is equal to 185.2 meters or 608 feet.

    - **Name**: "cable"
    - **Symbol**: "cbl"
    - **Meters per Unit**: 185.2

    More information about the cable unit can be found in the following resource:
    - [Cable on Wikipedia](https://en.wikipedia.org/wiki/Cable_(unit))
    """

    name: str = "cable"
    symbol: str = "cbl"
    meters_per_unit: float = 185.2
    metric_prefix: MetricPrefix = MetricPrefix.Base
    def __init__(self, *, _=None) -> None:
        # Must take metric prefix as an argument to conform to the LengthUnit class
        super().__init__(self.metric_prefix)


class Fathom(ImperialLengthUnit):
    """A class representing the fathom unit of length.

    The fathom is a unit of length used in maritime and navigation contexts.
    It is equal to 6 feet or 72 inches.

    - **Name**: "fathom"
    - **Symbol**: "ftm"
    - **Inches per Unit**: 72.0

    More information about the fathom unit can be found in the following resource:
    - [Fathom on Wikipedia](https://en.wikipedia.org/wiki/Fathom)
    """

    name: str = "fathom"
    symbol: str = "ftm"
    inches_per_unit: float = 72.0