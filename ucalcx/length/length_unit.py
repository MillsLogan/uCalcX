from ucalcx import Unit, Quantity, Unit, MetricPrefix


class LengthUnit(Unit):
    """ The base class for all length units. """
    
    def __init__(self, name: str, symbol: str, metric_prefix: 'MetricPrefix', conversion_factor: float):
        """ Initializes a new length unit. """
        
        super().__init__(name, symbol, metric_prefix, Quantity.Length)
        self.conversion_factor = conversion_factor
        """ The conversion factor to meters. I.e. 1 meter = conversion_factor * self. """
        
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

