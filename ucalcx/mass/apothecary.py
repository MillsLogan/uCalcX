from .mass_unit import MassUnit
from ucalcx import MetricPrefix


class Grain(MassUnit):
    symbol = 'gr'
    grams_per_unit = 0.06479891
    name = "grain"

    def __init__(self, metric_prefix: 'MetricPrefix'=MetricPrefix.Base):
        super().__init__(metric_prefix)


class Pennyweight(MassUnit):
    symbol = 'dwt'
    grams_per_unit = 1.55517384
    name = "pennyweight"

    def __init__(self, metric_prefix: 'MetricPrefix'=MetricPrefix.Base):
        super().__init__(metric_prefix)


class TroyOunce(MassUnit):
    symbol = 'oz_t'
    grams_per_unit = 31.1034768
    name = "troy ounce"

    def __init__(self, metric_prefix: 'MetricPrefix'=MetricPrefix.Base):
        super().__init__(metric_prefix)


class TroyPound(MassUnit):
    symbol = 'lb_t'
    grams_per_unit = 373.2417216
    name = "troy pound"

    def __init__(self, metric_prefix: 'MetricPrefix'=MetricPrefix.Base):
        super().__init__(metric_prefix)


class Carat(MassUnit):
    symbol = 'ct'
    grams_per_unit = 0.2
    name = "carat"

    def __init__(self, metric_prefix: 'MetricPrefix'=MetricPrefix.Base):
        super().__init__(metric_prefix)
