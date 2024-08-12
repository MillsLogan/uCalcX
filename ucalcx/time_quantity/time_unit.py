from common import FundamentalQuantity, FundamentalQuantityUnit, MetricPrefix



class FundamentalTimeUnit(FundamentalQuantityUnit):
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
microsecond = us = Second(MetricPrefix.Micro)
millisecond = ms = Second(MetricPrefix.Milli)
second = s = Second()
minute = min = FundamentalTimeUnit(name="minute", symbol="min", seconds_per_unit=60)
hour = h = FundamentalTimeUnit(name="hour", symbol="h", seconds_per_unit=3600)
day = d = FundamentalTimeUnit(name="day", symbol="d", seconds_per_unit=86400)
week = wk = FundamentalTimeUnit(name="week", symbol="wk", seconds_per_unit=604800)
fortnight = fn = FundamentalTimeUnit(name="fortnight", symbol="fn", seconds_per_unit=1209600)
month = mo = FundamentalTimeUnit(name="month", symbol="mo", seconds_per_unit=2629746)
year = yr = FundamentalTimeUnit(name="year", symbol="yr", seconds_per_unit=31556952)
decade = dec = FundamentalTimeUnit(name="decade", symbol="dec", seconds_per_unit=315569520)
century = cen = FundamentalTimeUnit(name="century", symbol="cen", seconds_per_unit=3155695200)
millennium = mil = FundamentalTimeUnit(name="millennium", symbol="mil", seconds_per_unit=31556952000)
