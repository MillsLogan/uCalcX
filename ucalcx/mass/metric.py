from ..common import MetricPrefix
from .mass_unit import FundamentalMassUnit


class Gram(FundamentalMassUnit):
    """ Represents a gram, the base unit of mass in the metric system. """
    
    def __init__(self, metric_prefix: MetricPrefix=MetricPrefix.Base):
        super().__init__(name="gram", symbol="g")
        self.metric_prefix = metric_prefix

    def grams_per_unit(self) -> float:
        return 10 ** self.metric_prefix.exponent

    @property
    def name(self) -> str:
        return f"{self.metric_prefix.name}{super().name}" 
    
    @property
    def symbol(self) -> str:
        return f"{self.metric_prefix.symbol}{super().symbol}"

gram = g = Gram()
""" Gram (g) - 10^0 grams """

kilogram = kg = Gram(metric_prefix=MetricPrefix.Kilo)
""" Kilogram (kg) - 10^3 grams """

milligram = mg = Gram(metric_prefix=MetricPrefix.Milli)
""" Milligram (mg) - 10^-3 grams """

microgram = ug = Gram(metric_prefix=MetricPrefix.Micro)
""" Microgram (ug) - 10^-6 grams """

tonne = t = Gram(metric_prefix=MetricPrefix.Mega)
""" Tonne (t) - 10^6 grams (also a Megagram or Mg) """




    
    