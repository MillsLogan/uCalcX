from common import MetricPrefix
from length import FundamentalLengthUnit


class Meter(FundamentalLengthUnit):
    def __init__(self, metric_prefix: MetricPrefix=MetricPrefix.Base, power: int=1):
        super().__init__(name="meter", symbol="m", power=power)
        self.metric_prefix = metric_prefix

    def meters_per_unit(self) -> float:
        return 10 ** self.metric_prefix.exponent

    @property
    def name(self) -> str:
        return f"{self.metric_prefix.name}{super().name}" 
    
    @property
    def symbol(self) -> str:
        return f"{self.metric_prefix.symbol}{super().symbol}"

# Common metric length units for convenience

millimeter = mm = Meter(MetricPrefix.Milli)
centimeter = cm = Meter(MetricPrefix.Centi)
meter = m = Meter()
kilometer = km = Meter(MetricPrefix.Kilo)




    
    