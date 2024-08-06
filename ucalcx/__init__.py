"""
# uCalcX Module

The `ucalcx` module is designed to provide a comprehensive unit conversion and calculation library. It includes various submodules for different physical quantities, such as length and time. Each submodule contains classes that represent specific units, allowing for accurate and convenient conversions and calculations.

## Overview

### Root Module

The `ucalcx` module serves as the entry point for the uCalcX library. It provides access to common classes and enumerations used across different physical quantities, such as units, metric prefixes, quantities, and measurements.

- `Measurement`: Represents a measurement, holding a value and a unit. Provides a `convert_to` method for converting between units.
- `Unit`: An abstract class that defines the required properties for a unit, such as name, symbol, metric prefix, and quantity.
- `MetricPrefix`: An enum that provides metric prefixes from yotta to yocto, along with their symbols and exponent values. Includes a `conversion_factor` method.
- `Quantity`: An enum representing the physical quantities that can be measured, ensuring that units are only converted within the same quantity type.

### Length Module

The `length` module provides classes for various units of length, categorized into different submodules:

- `metric`: Contains units from the metric system, such as meters, with support for metric prefixes.
- `imperial`: Contains units from the imperial system, such as inches, feet, yards, and miles.
- `nautical`: Contains units commonly used in nautical contexts, such as fathoms, nautical miles, and cables.
- `land`: Contains units used in land measurement, such as rods, chains, and furlongs.

Each class in the `length` module extends the `LengthUnit` class, which handles conversions to and from meters, allowing for consistent and precise calculations across different units.

### Time Module

The `time` module provides classes for various units of time. It includes:

- `Second`: The base unit of time in the metric system, with support for metric prefixes (e.g., milliseconds, microseconds).
- `Minute`: Represents the minute unit of time.
- `Hour`: Represents the hour unit of time.
- `Day`: Represents the day unit of time.
- `Week`: Represents the week unit of time.

Each class in the `time` module extends the `TimeUnit` class, which handles conversions to and from seconds, ensuring accurate time calculations and conversions.

Example:

The `ucalcx` module is designed for ease of use, allowing users to create measurements and convert between different units seamlessly. Below is a simple example of how to create a measurement and convert it:
>>> from ucalcx.length.metric import Meter
>>> from ucalcx.length.imperial import Mile
>>> from ucalcx import MetricPrefix

>>> # Create a measurement of 1 kilometer
>>> one_km = Measurement(1, Meter(MetricPrefix.Kilo))  # 1 kilometer

>>> # Convert from kilometers to miles
>>> one_km_in_miles = one_km.convert_to(Mile())  # Convert to miles
>>> print(f"{one_km} is equal to {one_km_in_miles}")
1 km is equal to 0.621371192237334 mi
"""


from ucalcx.common import *


__all__ = ['MetricPrefix', 'Unit', 'Quantity', 'Measurement']