"""
# length Module

The `length` module provides classes for units of length across various measurement systems. It includes support for metric and non-metric units, with the ability to apply metric prefixes. The module is organized into submodules, each focusing on different systems or contexts of length measurement.

## Submodules:

- **metric**: Provides metric units of length. Includes units like Meter, Kilometer, Centimeter, etc.
- **imperial**: Provides units of length used in the US Customary and British Imperial systems. Includes units like Foot, Yard, Mile, Inch, Thou, and Hand.
- **nautical**: Provides units of length used primarily in maritime and navigation contexts. Includes units like Fathom, Nautical Mile, and Cable.
- **land**: Provides units of length used in land measurement and surveying. Includes units like Rod, Chain, and Furlong.

## Overview:

This module extends `LengthUnit` and supports metric prefixes for all units. It is designed to facilitate conversions and calculations involving length units across different systems, while allowing for optional metric prefix adjustments.

## External Resources:
- [Metric System Overview](https://en.wikipedia.org/wiki/Metric_system)
- [Imperial Units Overview](https://en.wikipedia.org/wiki/Imperial_units)
- [Nautical Units Overview](https://en.wikipedia.org/wiki/Nautical_mile)
- [Land Measurement Units Overview](https://en.wikipedia.org/wiki/Chain_(unit))
"""

from ucalcx.length.length_unit import LengthUnit
from ucalcx.length import metric, imperial, nautical, land

__all__ = ['LengthUnit', 'imperial', 'metric', 'nautical', 'land']

