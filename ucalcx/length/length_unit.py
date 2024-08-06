from ucalcx import Unit, Quantity, Unit, MetricPrefix
from abc import ABC, abstractmethod


class LengthUnit(Unit):
    """ The base class for all length units. """
    
    def __init__(self, name: str, symbol: str, metric_prefix: 'MetricPrefix', conversion_factor: float):
        """ Initializes a new length unit. """
        
        super().__init__(name, symbol, metric_prefix, Quantity.Length)
        self.conversion_factor = conversion_factor
        
    def _convert_to_meters(self, value: float) -> float:
        """ Converts a value to meters. """
        
        return value * self.conversion_factor
    
    def _convert_from_meters(self, value: float) -> float:
        """ Converts a value from meters. """
        
        return value / self.conversion_factor
        
    def convert_to(self, other: 'LengthUnit', value: float) -> float:
        """ 
        Converts a value from this length unit to another length unit. 
        
        Args:
        - other: The length unit to convert the value to.
        - value: The value to convert.
        
        Returns:
        - The converted value.
        """
        
        converted_value = self._convert_to_meters(value)
        if other.metric_prefix != self.metric_prefix:
            converted_value = self.metric_prefix.convert_to(other.metric_prefix, converted_value)
        return other._convert_from_meters(converted_value)
    
    
class Meter(LengthUnit):
    """ The meter is the base unit of length in the International System of Units (SI). """
    
    def __init__(self, metric_prefix: 'MetricPrefix' = MetricPrefix.Base):
        """ Initializes a new meter unit. """
        
        super().__init__('Meter', 'm', metric_prefix, 1)
    
    
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
    