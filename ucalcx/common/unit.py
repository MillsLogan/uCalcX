class Unit:
    """
    # Unit Class

    An abstract class that defines the required properties for a unit of measurement. Units can be characterized by their name, symbol, metric prefix, and the physical quantity they measure.

    Parameters:
        name (str): The name of the unit (e.g., "meter").
        symbol (str): The symbol of the unit (e.g., "m").
        metric_prefix (MetricPrefix): The metric prefix associated with the unit.
        quantity (Quantity): The physical quantity that the unit measures.
    
    ## Properties:
    - `full_name`: The full name of the unit, including the metric prefix. (e.g., "kilometer")
    - `full_symbol`: The full symbol of the unit, including the metric prefix. (e.g., "km")
    """
    name: str
    symbol: str
    metric_prefix: 'MetricPrefix'
    quantity: 'Quantity'
    
    def __init__(self, metric_prefix: 'MetricPrefix') -> None:
        """
        Initializes a new instance of the Unit class.

        Args:
            name (str): The name of the unit (e.g., "meter", "second"). This is a descriptive term for the unit.
            symbol (str): The symbol of the unit (e.g., "m" for meter, "s" for second). This is the abbreviated representation of the unit.
            metric_prefix (MetricPrefixes): The metric prefix associated with the unit, specifying the magnitude (e.g., `MetricPrefixes.Kilo` for kilo, `MetricPrefixes.Milli` for milli). The prefix modifies the base unit to represent different scales.
            quantity (Quantity): The physical quantity that the unit measures (e.g., `Quantity.Length` for length, `Quantity.Time` for time). This determines what kind of measurement the unit represents.
        """
        
        self.metric_prefix = metric_prefix
    
    @classmethod
    def make_custom_unit(cls, name: str, symbol: str, metric_prefix: 'MetricPrefix', quantity: 'Quantity') -> 'Unit':
        """
        Creates a custom unit with the specified name, symbol, and conversion factor to meters.

        Args:
            name (str): The name of the custom unit.
            symbol (str): The symbol of the custom unit.
            meters_per_unit (float): The conversion factor to convert this unit to meters.
            metric_prefix (MetricPrefix): The metric prefix to apply to the custom unit.

        Returns:
            Unit: A custom unit object with the specified properties.
        """
        
        custom_unit = cls(metric_prefix)
        custom_unit.name = name
        custom_unit.symbol = symbol
        custom_unit.quantity = quantity
        
        return custom_unit

    @property
    def full_name(self) -> str:
        """ Returns the name of the unit with the metric prefix name prepended. """
        
        return f"{self.metric_prefix.name}{self.name}"
    
    @property
    def full_symbol(self) -> str:
        """ Returns the symbol of the unit with the metric prefix symbol prepended. """
        
        return f"{self.metric_prefix.symbol}{self.symbol}"
    
    def __str__(self) -> str:
        return f"{self.full_name} ({self.full_symbol})"
    