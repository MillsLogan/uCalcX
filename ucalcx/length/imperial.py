from ucalcx.common import MetricPrefix
from .length_unit import LengthUnit        


class Inch(LengthUnit):
    """ The inch is a unit of length in the imperial and US customary systems of measurement. """
    
    def __init__(self, metric_prefix: MetricPrefix = MetricPrefix.Base):
        """ Initializes a new inch unit. """
        
        super().__init__('Inch', 'in', metric_prefix, 0.0254)
    
    
class Foot(LengthUnit):
    """ The foot is a unit of length in the imperial and US customary systems of measurement. """
    
    def __init__(self, metric_prefix: MetricPrefix = MetricPrefix.Base):
        """ Initializes a new foot unit. """
        
        super().__init__('Foot', 'ft', metric_prefix, 0.3048)
        

class Yard(LengthUnit):
    """ The yard is a unit of length in the imperial and US customary systems of measurement. """
    
    def __init__(self, metric_prefix: MetricPrefix = MetricPrefix.Base):
        """ Initializes a new yard unit. """
        
        super().__init__('Yard', 'yd', metric_prefix, 0.9144)
        

class Mile(LengthUnit):
    """ The mile is a unit of length in the imperial and US customary systems of measurement. """
    
    def __init__(self, metric_prefix: MetricPrefix = MetricPrefix.Base):
        """ Initializes a new mile unit. """
        
        super().__init__('Mile', 'mi', metric_prefix, 1609.344)
