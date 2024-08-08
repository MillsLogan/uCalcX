from .mass_unit import MassUnit
from ucalcx import MetricPrefix

class Gram(MassUnit):

    symbol = 'g'
    grams_per_unit = 1.0
    name = "gram"
    
    def __init__(self, metric_prefix: 'MetricPrefix'=MetricPrefix.Base):
        
        
        super().__init__(metric_prefix)    
