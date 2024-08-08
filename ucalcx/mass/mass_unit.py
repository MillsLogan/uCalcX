from ucalcx import Unit, Quantity, Unit, MetricPrefix


class MassUnit(Unit):
    name: str
    symbol: str
    grams_per_unit: float
    quantity: Quantity = Quantity.Mass
    
    def __init__(self, metric_prefix: 'MetricPrefix') -> None:
        
        super().__init__(metric_prefix) 
        
    def convert_to(self, other: 'MassUnit', value: float) -> float:
        
        if other.quantity != Quantity.Mass:
            raise ValueError("Cannot convert between different quantities")

        this_to_other_factor: float = self.grams_per_unit / other.grams_per_unit
        converted_value: float = value * this_to_other_factor
        if other.metric_prefix != self.metric_prefix:
            converted_value = self.metric_prefix.convert_to(other.metric_prefix, converted_value)
        return converted_value        

