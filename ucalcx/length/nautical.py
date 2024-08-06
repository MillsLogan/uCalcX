from .length_unit import LengthUnit
from ucalcx import MetricPrefix

      
class NauticalMile(LengthUnit):
    """ The nautical mile is a unit of length used in navigation. """

    def __init__(self, metric_prefix: MetricPrefix = MetricPrefix.Base):
        """ Initializes a new nautical mile unit. """

        super().__init__('Nautical Mile', 'nmi', metric_prefix, 1852)
        
        
class Fathom(LengthUnit):
    """ The fathom is a unit of length used in navigation. """
    
    def __init__(self, metric_prefix: MetricPrefix = MetricPrefix.Base):
        """ Initializes a new fathom unit. """
        
        super().__init__('Fathom', 'ftm', metric_prefix, 1.8288)
        
        
class Cable(LengthUnit):
    """ The cable is a unit of length used in navigation. """
    
    def __init__(self, metric_prefix: MetricPrefix = MetricPrefix.Base):
        """ Initializes a new cable unit. """
        
        super().__init__('Cable', 'cbl', metric_prefix, 185.2)