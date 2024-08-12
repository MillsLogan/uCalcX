from common import MetricPrefix
from .mass_unit import FundamentalMassUnit


class Gram(FundamentalMassUnit):
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
kilogram = kg = Gram(metric_prefix=MetricPrefix.Kilo)
milligram = mg = Gram(metric_prefix=MetricPrefix.Milli)
microgram = ug = Gram(metric_prefix=MetricPrefix.Micro)
tonne = t = Gram(metric_prefix=MetricPrefix.Mega)




    
    