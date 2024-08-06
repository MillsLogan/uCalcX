from .length_unit import LengthUnit
from ucalcx import MetricPrefix

class Meter(LengthUnit):
    """ The meter is the base unit of length in the International System of Units (SI). """
    
    def __init__(self, metric_prefix: 'MetricPrefix' = MetricPrefix.Base):
        """ Initializes a new meter unit. """
        
        super().__init__('Meter', 'm', metric_prefix, 1)