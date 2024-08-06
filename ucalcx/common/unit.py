class Unit:
    """ 
    The base class for all units. A unit is a standard quantity used to express physical quantities.
    A unit has a name, symbol, metric prefix, and quantity.

    Attributes:
    - name (`str`): The name of the unit.
    - symbol (`str`): The symbol of the unit.
    - metric_prefix (`str`): The metric prefix of the unit.
    - quantity (`Quantity`): The quantity of the unit.
    """
    
    def __init__(self, name: str, symbol: str, metric_prefix: 'MetricPrefix', quantity: 'Quantity'):
        """ Initializes a new unit. """
        
        self.name = name
        self.symbol = symbol
        self.metric_prefix = metric_prefix
        self.quantity = quantity
    
    @property
    def full_name(self) -> str:
        """ Returns the full name of the unit, including the metric prefix. """
        
        return f"{self.metric_prefix.name}{self.name}"
    
    @property
    def full_symbol(self) -> str:
        """ Returns the full symbol of the unit, including the metric prefix. """
        
        return f"{self.metric_prefix.symbol}{self.symbol}"
    