from dataclasses import dataclass


@dataclass(frozen=True, eq=True)
class Measurement:
    """
    A class representing a measurement.
    
    Each measurement has:
    - value: The value of the measurement.
    - unit: The unit of the measurement.
    
    Each measurement can be converted to another unit by using the convert_to method.
    """
    
    value: float
    """ The value of the measurement. """
    
    unit: 'Unit'
    """ The unit of the measurement. """
    
    def convert_to(self, other: 'Unit') -> 'Measurement':
        """ 
        Converts the measurement to another unit. 
        
        Args:
        - other: The unit to convert the measurement to.
        
        Returns:
        - The converted measurement.
        """
        
        if other.quantity != self.unit.quantity:
            raise ValueError(f"Cannot convert {self.unit.quantity.name} to {other.quantity.name}.")
        
        converted_value = self.unit.convert_to(other, self.value)
        return Measurement(converted_value, other)
