from ..common import FundamentalQuantity, FundamentalQuantityUnit, MetricPrefix


class FundamentalTimeUnit(FundamentalQuantityUnit):
    """ A base class for units of time. This class should not be instantiated directly. """
    
    def __init__(self, name: str, symbol: str, seconds_per_unit):
        super().__init__(name=name, symbol=symbol, quantity=FundamentalQuantity.Time)
        self._seconds_per_unit = seconds_per_unit

    def _conversion_method(self, other: "FundamentalTimeUnit", value: float) -> float:
        if not isinstance(other, FundamentalTimeUnit):
            raise ValueError(f"Tried to convert {self} to {other}. Expected two time units.")
        
        return value * self.seconds_per_unit() / other.seconds_per_unit()
    
    def seconds_per_unit(self) -> float:
        return self._seconds_per_unit
    

class Second(FundamentalTimeUnit):
    """ Represents a second. """
    
    def __init__(self, metric_prefix=MetricPrefix.Base):
        super().__init__(name="second", symbol="s", seconds_per_unit=1.0)
        self.metric_prefix = metric_prefix

    def seconds_per_unit(self) -> float:
        return 10 ** self.metric_prefix.exponent
    
    @property
    def name(self):
        return f"{self.metric_prefix.name}{super().name}"
    
    @property
    def symbol(self):
        return f"{self.metric_prefix.symbol}{super().symbol}"
    
    
nanosecond = ns = Second(MetricPrefix.Nano)
""" Nanosecond (ns) - 10^-9 seconds """

microsecond = us = Second(MetricPrefix.Micro)
""" Microsecond (us) - 10^-6 seconds """

millisecond = ms = Second(MetricPrefix.Milli)
""" Millisecond (ms) - 10^-3 seconds """

second = s = Second()
""" Second (s) - 10^0 seconds """

minute = min = FundamentalTimeUnit(name="minute", symbol="min", seconds_per_unit=60)
""" Minute (min) - 60 seconds """

hour = h = FundamentalTimeUnit(name="hour", symbol="h", seconds_per_unit=3600)
""" Hour (h) - 3600 seconds """

day = d = FundamentalTimeUnit(name="day", symbol="d", seconds_per_unit=86400)
""" Day (d) - 86400 seconds """

week = wk = FundamentalTimeUnit(name="week", symbol="wk", seconds_per_unit=604800)
""" Week (wk) - 604800 seconds """

fortnight = fn = FundamentalTimeUnit(name="fortnight", symbol="fn", seconds_per_unit=1209600)
""" Fortnight (fn) - 1209600 seconds """

month = mo = FundamentalTimeUnit(name="month", symbol="mo", seconds_per_unit=2629746)
""" Month (mo) - 2629746 seconds """

year = yr = FundamentalTimeUnit(name="year", symbol="yr", seconds_per_unit=31556952)
""" Year (yr) - 31556952 seconds """

decade = dec = FundamentalTimeUnit(name="decade", symbol="dec", seconds_per_unit=315569520)
""" Decade (dec) - 315569520 seconds """

century = cen = FundamentalTimeUnit(name="century", symbol="cen", seconds_per_unit=3155695200)
""" Century (cen) - 3155695200 seconds """

millennium = mil = FundamentalTimeUnit(name="millennium", symbol="mil", seconds_per_unit=31556952000)
""" Millennium (mil) - 31556952000 seconds """

