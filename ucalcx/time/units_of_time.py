from .time_unit import TimeUnit
from ucalcx import MetricPrefix


class Second(TimeUnit):
    """
    Represents the second unit of time, the base unit in the International System of Units (SI). This class extends `TimeUnit` to provide a specific implementation of the second unit.

    - **Name**: "second"
    - **Symbol**: "s"
    - **Conversion Factor**: 1.0 (as it represents the base second unit)

    Args:
        metric_prefix (MetricPrefix, optional): The metric prefix to apply to the second unit. Defaults to `MetricPrefix.Base`, representing the base second unit.

    For more information about the second and its usage, refer to the following resource:
    - [Second on Wikipedia](https://en.wikipedia.org/wiki/Second)
    """

    name: str = "second"
    symbol: str = "s"
    seconds_per_unit: float = 1.0

    def __init__(self, metric_prefix: MetricPrefix=MetricPrefix.Base) -> None:
        """
        Initializes a Second object with an optional metric prefix.

        Args:
            metric_prefix (MetricPrefix): The metric prefix to apply to the minute unit. Defaults to `MetricPrefix.Base`.
        """

        super().__init__(metric_prefix)        


class Minute(TimeUnit):
    """
    Represents the minute unit of time, commonly used in everyday contexts.

    - **Name**: "minute"
    - **Symbol**: "min"
    - **Seconds per Unit**: 60.0

    Args:
        metric_prefix (MetricPrefix): The metric prefix to apply to the minute unit. Defaults to `MetricPrefix.Base`.

    For more information about the minute and its usage, refer to the following resource:
    - [Minute on Wikipedia](https://en.wikipedia.org/wiki/Minute)
    """

    name: str = "minute"
    symbol: str = "min"
    seconds_per_unit: float = 60.0

    def __init__(self, metric_prefix: MetricPrefix=MetricPrefix.Base) -> None:
        """
        Initializes a Minute object with an optional metric prefix.

        Args:
            metric_prefix (MetricPrefix): The metric prefix to apply to the minute unit. Defaults to `MetricPrefix.Base`.
        """

        super().__init__(metric_prefix)


class Hour(TimeUnit):
    """
    Represents the hour unit of time, commonly used in everyday contexts.

    - **Name**: "hour"
    - **Symbol**: "h"
    - **Seconds per Unit**: 3600.0

    Args:
        metric_prefix (MetricPrefix): The metric prefix to apply to the hour unit. Defaults to `MetricPrefix.Base`.

    For more information about the hour and its usage, refer to the following resource:
    - [Hour on Wikipedia](https://en.wikipedia.org/wiki/Hour)
    """

    name: str = "hour"
    symbol: str = "h"
    seconds_per_unit: float = 3600.0

    def __init__(self, metric_prefix: MetricPrefix=MetricPrefix.Base) -> None:
        """
        Initializes an Hour object with an optional metric prefix.

        Args:
            metric_prefix (MetricPrefix): The metric prefix to apply to the hour unit. Defaults to `MetricPrefix.Base`.

        Example:
            >>> from ucalcx.time import Hour
            >>> hour = Hour()
            >>> print(hour.full_name)
            hour
            >>> print(hour.symbol)
            h
        """
        
        super().__init__(metric_prefix)


class Day(TimeUnit):
    """
    Represents the day unit of time, commonly used in everyday contexts.

    - **Name**: "day"
    - **Symbol**: "d"
    - **Seconds per Unit**: 86400.0

    Args:
        metric_prefix (MetricPrefix): The metric prefix to apply to the day unit. Defaults to `MetricPrefix.Base`.

    For more information about the day and its usage, refer to the following resource:
    - [Day on Wikipedia](https://en.wikipedia.org/wiki/Day)
    """

    name: str = "day"
    symbol: str = "d"
    seconds_per_unit: float = 86400.0

    def __init__(self, metric_prefix: MetricPrefix=MetricPrefix.Base) -> None:
        """
        Initializes a Day object with an optional metric prefix.

        Args:
            metric_prefix (MetricPrefix): The metric prefix to apply to the day unit. Defaults to `MetricPrefix.Base`.
        """

        super().__init__(metric_prefix)


class Week(TimeUnit):
    """
    Represents the week unit of time, commonly used in everyday contexts.

    - **Name**: "week"
    - **Symbol**: "wk"
    - **Seconds per Unit**: 604800.0

    Args:
        metric_prefix (MetricPrefix): The metric prefix to apply to the week unit. Defaults to `MetricPrefix.Base`.

    For more information about the week and its usage, refer to the following resource:
    - [Week on Wikipedia](https://en.wikipedia.org/wiki/Week)
    """

    name: str = "week"
    symbol: str = "wk"
    seconds_per_unit: float = 604800.0

    def __init__(self, metric_prefix: MetricPrefix=MetricPrefix.Base) -> None:
        """
        Initializes a Week object with an optional metric prefix.

        Args:
            metric_prefix (MetricPrefix): The metric prefix to apply to the week unit. Defaults to `MetricPrefix.Base`.
        """

        super().__init__(metric_prefix)


class Month(TimeUnit):
    """
    Represents the month unit of time, commonly used in everyday contexts.

    - **Name**: "month"
    - **Symbol**: "mo"
    - **Seconds per Unit**: Approximately 2,629,746.0 (based on the average length of a month)

    Args:
        metric_prefix (MetricPrefix): The metric prefix to apply to the month unit. Defaults to `MetricPrefix.Base`.

    For more information about the month and its usage, refer to the following resource:
    - [Month on Wikipedia](https://en.wikipedia.org/wiki/Month)
    """

    name: str = "month"
    symbol: str = "mo"
    seconds_per_unit: float = 2592000

    def __init__(self, metric_prefix: MetricPrefix=MetricPrefix.Base) -> None:
        """
        Initializes a Month object with an optional metric prefix.

        Args:
            metric_prefix (MetricPrefix): The metric prefix to apply to the month unit. Defaults to `MetricPrefix.Base`.
        """

        super().__init__(metric_prefix)


class Year(TimeUnit):
    """
    Represents the year unit of time, commonly used in everyday contexts.

    - **Name**: "year"
    - **Symbol**: "yr"
    - **Seconds per Unit**: Approximately 31,557,600.0 (based on the average length of a year)

    Args:
        metric_prefix (MetricPrefix): The metric prefix to apply to the year unit. Defaults to `MetricPrefix.Base`.

    For more information about the year and its usage, refer to the following resource:
    - [Year on Wikipedia](https://en.wikipedia.org/wiki/Year)
    """

    name: str = "year"
    symbol: str = "yr"
    seconds_per_unit: float = 31536000

    def __init__(self, metric_prefix: MetricPrefix=MetricPrefix.Base) -> None:
        """
        Initializes a Year object with an optional metric prefix.

        Args:
            metric_prefix (MetricPrefix): The metric prefix to apply to the year unit. Defaults to `MetricPrefix.Base`.
        """

        super().__init__(metric_prefix)


