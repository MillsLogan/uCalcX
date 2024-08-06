"""
# uCalcX Module

The `uCalcX` module provides a comprehensive suite of tools for unit conversion and measurement calculations. It is designed to be modular and extensible, allowing for easy integration of various measurement types and unit systems.

Common Module:
    The `common` module contains fundamental classes and enumerations used throughout the `uCalcX` library. It defines essential concepts and provides the building blocks for representing measurements, units, and physical quantities. All classes and enums are directly importable from the `ucalcx` module, however, you may look at the `common` module for detailed documentation and implementation details.

    Submodules:
        - measurement: Defines the `Measurement` class for representing a value and its associated unit.
        - unit: Provides the abstract `Unit` class for defining units of measurement and their properties.
        - metric_prefixes: Contains the `MetricPrefixes` enum for metric prefixes and conversion factors.
        - quantity: Includes the `Quantity` enum for defining different physical quantities.

Length Module:
    The `length` module (to be documented) will provide specific units and conversions related to length measurements, including common units like meters, kilometers, and other length-related units.

Expansion:
    Additional modules and features will be documented as they are developed. Future expansions may include modules for time, mass, temperature, and other physical quantities, along with their specific units and conversion methods.

Example Usage:
    Here's a brief example of how to use the `common` module to create and convert measurements:

    >>> from ucalcx.common import Measurement, MetricPrefixes
    >>> length = Measurement(5.0, Unit("meter", "m", MetricPrefixes.None_, Quantity.Length))
    >>> length_in_kilometers = length.convert_to(Unit("kilometer", "km", MetricPrefixes.Kilo, Quantity.Length))
    >>> print(length_in_kilometers.value)
    0.005
    >>> print(length_in_kilometers.unit.full_symbol)
    km
"""


from ucalcx.common import *


__all__ = ['MetricPrefix', 'Unit', 'Quantity', 'Measurement']