from .quantity import FundamentalQuantity
from .quantity_component import QuantityComponent

class Unit:
    def __init__(self, dimension: dict[FundamentalQuantity, QuantityComponent]):
        self.dimension: dict[FundamentalQuantity, QuantityComponent] = dimension
    
    @classmethod
    def from_quantity_components(cls, *components: QuantityComponent) -> "Unit":
        dimensions = {quantity: None for quantity in FundamentalQuantity}
        for component in components:
            if dimensions[component.quantity] is not None:
                raise ValueError(f"Cannot have multiple components for the same quantity: {component.quantity}")
            dimensions[component.quantity] = component
        return cls(dimensions)

    @property
    def components(self) -> list[QuantityComponent]:
        return [component for component in self.dimension.values() if component is not None]

    @property
    def name(self) -> str:
        numerator = []
        denominator = []
        for component in self.components:
            if component is None:
                continue
            if component.power > 0:
                numerator.append(component.unit.name)
            elif component.power < 0:
                denominator.append(component.unit.name)
        if not numerator:
            numerator.append("1")
        return f"{'*'.join(numerator)}{'/' + '*'.join(denominator) if denominator else ''}".replace("-", "")

    @property
    def symbol(self) -> str:
        numerator = []
        denominator = []
        for component in self.components:
            if component is None:
                continue
            if component.power > 0:
                numerator.append(component.unit.symbol)
            elif component.power < 0:
                denominator.append(component.unit.symbol)
        if not numerator:
            numerator.append("1")
        return f"{'*'.join(numerator)}{'/' + '*'.join(denominator) if denominator else ''}".replace("-", "")
    
    def __str__(self):
        return f"{self.name} ({self.symbol})"
                
    
    
