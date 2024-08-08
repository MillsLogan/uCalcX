from .mass_unit import MassUnit
from ucalcx import MetricPrefix


class Dalton(MassUnit):
    symbol = 'Da'
    grams_per_unit = 1.66053906660e-24
    name = "dalton"

    def __init__(self, metric_prefix: 'MetricPrefix'=MetricPrefix.Base):
        super().__init__(metric_prefix)


class AtomicMassUnit(MassUnit):
    symbol = 'amu'
    grams_per_unit = 1.66053906660e-24
    name = "atomic_mass_unit"

    def __init__(self, metric_prefix: 'MetricPrefix'=MetricPrefix.Base):
        super().__init__(metric_prefix)