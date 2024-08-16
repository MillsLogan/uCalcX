from ..common import MetricPrefix
from .length_unit import FundamentalLengthUnit


class Meter(FundamentalLengthUnit):
    """ Represents a meter, the base unit of length in the metric system. 
    
    Args:
        metric_prefix (MetricPrefix): The metric prefix to use with the meter unit. Defaults to 
            MetricPrefix.Base.
    """
    
    def __init__(self, metric_prefix: MetricPrefix=MetricPrefix.Base):
        super().__init__(name="meter", symbol="m")
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
""" Millimeter (mm) - 10^-3 meters """

centimeter = cm = Meter(MetricPrefix.Centi)
""" Centimeter (cm) - 10^-2 meters """

meter = m = Meter()
""" Meter (m) - 10^0 meters """

kilometer = km = Meter(MetricPrefix.Kilo)
""" Kilometer (km) - 10^3 meters """



    
    