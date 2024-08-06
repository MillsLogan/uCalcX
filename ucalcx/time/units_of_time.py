from .time_unit import TimeUnit
from ucalcx import MetricPrefix


class Second(TimeUnit):
    """
    Represents the second unit of time, the base unit in the International System of Units (SI). This class extends `TimeUnit` to provide a specific implementation of the second unit.

    - **Name**: "Second"
    - **Symbol**: "s"
    - **Conversion Factor**: 1.0 (as it represents the base second unit)

    Args:
        metric_prefix (MetricPrefix, optional): The metric prefix to apply to the second unit. Defaults to `MetricPrefix.Base`, representing the base second unit.

    For more information about the second and its usage, refer to the following resource:
    - [Second on Wikipedia](https://en.wikipedia.org/wiki/Second)
    """

    def __init__(self, metric_prefix: MetricPrefix=MetricPrefix.Base) -> None:
        """
        Initializes the Second unit.
        
        The Second unit is the base time unit, representing 1 second.
        """

        super().__init__('second', 's', metric_prefix, 1)        


class Minute(TimeUnit):
    """
    Represents the minute unit of time.

    One minute is equivalent to 60 seconds.

    Attributes:
        name (str): The name of the unit, which is "Minute".
        symbol (str): The symbol for the unit, which is "min".
        seconds_per_unit (int): The number of seconds that one minute represents, which is 60.

    External Resource:
        - [Minute - Wikipedia](https://en.wikipedia.org/wiki/Minute)
    """

    def __init__(self, metric_prefix: MetricPrefix=MetricPrefix.Base) -> None:
        """
        Initializes the Minute unit.
        
        The Minute unit represents 60 seconds.
        """

        super().__init__('minute', 'min', metric_prefix, 60)


class Hour(TimeUnit):
    def __init__(self, metric_prefix: MetricPrefix=MetricPrefix.Base) -> None:
        super().__init__('hour', 'h', metric_prefix, 3600)


class Day(TimeUnit):
    def __init__(self, metric_prefix: MetricPrefix=MetricPrefix.Base) -> None:
        super().__init__('day', 'd', metric_prefix, 86400)


class Week(TimeUnit):
    def __init__(self, metric_prefix: MetricPrefix=MetricPrefix.Base) -> None:
        super().__init__('week', 'wk', metric_prefix, 604800)


class Month(TimeUnit):
    def __init__(self, metric_prefix: MetricPrefix=MetricPrefix.Base) -> None:
        super().__init__('month', 'mo', metric_prefix, 2592000)


class Year(TimeUnit):
    def __init__(self, metric_prefix: MetricPrefix=MetricPrefix.Base) -> None:
        super().__init__('year', 'yr', metric_prefix, 31536000)


