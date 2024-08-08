from .mass_unit import MassUnit
from ucalcx import MetricPrefix


class Ounce(MassUnit):
    symbol = 'oz'
    grams_per_unit = 28.3495
    name = "ounce"

    def __init__(self, metric_prefix: 'MetricPrefix'=MetricPrefix.Base):
        super().__init__(metric_prefix)
        

class Pound(MassUnit):
    symbol = 'lb'
    grams_per_unit = 453.592
    name = "pound"

    def __init__(self, metric_prefix: 'MetricPrefix'=MetricPrefix.Base):
        super().__init__(metric_prefix)


class Stone(MassUnit):
    symbol = 'st'
    grams_per_unit = 6350.29
    name = "stone"

    def __init__(self, metric_prefix: 'MetricPrefix'=MetricPrefix.Base):
        super().__init__(metric_prefix)


class ShortTon(MassUnit):
    symbol = 'tn'
    grams_per_unit = 907184.74
    name = "short_ton"

    def __init__(self, metric_prefix: 'MetricPrefix'=MetricPrefix.Base):
        super().__init__(metric_prefix)


class LongTon(MassUnit):
    symbol = 'LT'
    grams_per_unit = 1016046.91
    name = "long_ton"

    def __init__(self, metric_prefix: 'MetricPrefix'=MetricPrefix.Base):
        super().__init__(metric_prefix)


class Slug(MassUnit):
    symbol = 'slug'
    grams_per_unit = 14593.9
    name = "slug"

    def __init__(self, metric_prefix: 'MetricPrefix'=MetricPrefix.Base):
        super().__init__(metric_prefix)

