"""Provides a collection of length units across different measurement systems and domains.

This module contains classes representing various length units used in different measurement 
systems and domains, such as the metric system, imperial system, nautical system, and land measurement. 
Each class provides information about the unit, such as its name, symbol, and conversion factors to other units.
Every class is a subclass of the `LengthUnit` class, which provides a common interface for working with
different units of length. This means that all units can be used interchangeably in calculations and conversions,
taking the complexity out of working with different measurement systems.

For more information about the different measurement systems and their units, refer to the following resources:
- [Metric System on Wikipedia](https://en.wikipedia.org/wiki/Metric_system)
- [Imperial System on Wikipedia](https://en.wikipedia.org/wiki/Imperial_units)
- [Nautical System on Wikipedia](https://en.wikipedia.org/wiki/Nautical_system)
- [Land Measurement on Wikipedia](https://en.wikipedia.org/wiki/English_units)

Example:
    To use a specific length unit, import the corresponding class and create an instance of it:

    >>> from ucalcx.length.metric import Meter
    >>> meter = Meter()
    >>> print(meter)
    meter (m)

    >>> from ucalcx.length.imperial import Foot
    >>> foot = Foot()
    >>> print(foot)
    foot (ft)

    >>> from ucalcx.length.nautical import NauticalMile
    >>> nautical_mile = NauticalMile()
    >>> print(nautical_mile)
    nautical_mile (NM)

    >>> from ucalcx.length.land import Chain
    >>> chain = Chain()
    >>> print(chain)
    chain (ch)

    You can also perform conversions between different units using the `convert_to` method:

    >>> value = 100.0
    >>> meters = meter.convert_to(Foot(), value)
    >>> print(f"{value} meters is equal to {meters} feet.")
    100.0 meters is equal to 328.084 feet.

    uCalcX also provides implicit conversions between units when performing arithmetic operations
    see the `Measurement` class and the root `ucalcx` package for more information and examples.
"""

from ucalcx.length.length_unit import LengthUnit
from ucalcx.length import metric, imperial, nautical, land
from ucalcx.length.imperial import ImperialLengthUnit

__all__ = ['LengthUnit', 'imperial', 'metric', 'nautical', 'land']

def get_all_units():
    import inspect
    """
    Returns a list of all available length units across the different measurement systems.

    Returns:
        list: A list of all available length units.
    """

    all_units = []
    all_units.extend(inspect.getmembers(metric, lambda x: inspect.isclass(x) and issubclass(x, LengthUnit) and x != LengthUnit and x != ImperialLengthUnit))
    all_units.extend(inspect.getmembers(imperial, lambda x: inspect.isclass(x) and issubclass(x, LengthUnit) and x != LengthUnit and x != ImperialLengthUnit))
    all_units.extend(inspect.getmembers(nautical, lambda x: inspect.isclass(x) and issubclass(x, LengthUnit) and x != LengthUnit and x != ImperialLengthUnit))
    all_units.extend(inspect.getmembers(land, lambda x: inspect.isclass(x) and issubclass(x, LengthUnit) and x != LengthUnit and x != ImperialLengthUnit))
    return list(map(lambda x: x[1], all_units))