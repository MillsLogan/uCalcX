"""
# time Module

The `time` module provides classes for various units of time and their conversions. 

## Time Units:

- **Second (s)**: The base unit of time in the International System of Units (SI).
- **Minute (min)**: Represents 60 seconds.
- **Hour (h)**: Represents 60 minutes, or 3,600 seconds.
- **Day (d)**: Represents 24 hours, or 86,400 seconds.
- **Week (wk)**: Represents 7 days, or 604,800 seconds.
- **Month (mo)**: Represents approximately 30 days, or 2,592,000 seconds.
- **Year (yr)**: Represents 365 days, or 31,536,000 seconds, with adjustments for leap years.

## Metric Prefixes:

For finer measurements of time, such as milliseconds, microseconds, and nanoseconds, you can use the metric prefixes of the `Second` class. This allows for precise measurement without needing separate classes for each small time unit.

Example:

>>> from ucalcx.time import Second, Minute, Hour
>>> # Create unit instances
>>> minute = Minute()
>>> # Create a measurement of 2 minutes
>>> measurement = Measurement(2, minute)
>>> print(measurement)
2 min
>>> # Convert the measurement to hours
>>> measurement_in_hours = measurement.convert_to(Hour())
>>> print(measurement_in_hours)
0.03333333333333333 h
"""


from .time_unit import TimeUnit
from .units_of_time import Second, Minute, Hour, Day, Week, Month, Year

__all__ = ["TimeUnit", "Second", "Minute", "Hour", "Day", "Week", "Month", "Year"]