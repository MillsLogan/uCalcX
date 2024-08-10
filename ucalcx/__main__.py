from common import QuantityComponent, Unit, FundamentalQuantityUnit
from length import metric, imperial
from common import FundamentalQuantity


class FundamentalTimeUnit(FundamentalQuantityUnit):
    def __init__(self, name: str, symbol: str, power: int=1):
        super().__init__(name=name, symbol=symbol, quantity=FundamentalQuantity.Time, power=power)
    
    def seconds_per_unit(self) -> float:
        return 1.0
    
    def _conversion_method(self, other: "FundamentalTimeUnit", value: float) -> float:
        if not isinstance(other, FundamentalTimeUnit):
            raise ValueError(f"Tried to convert {self} to {other}. Expected two time units.")
        
        this_to_other_factor = self.seconds_per_unit() / other.seconds_per_unit()
        
        return value * (this_to_other_factor ** self.power)


def main():
    ten_meters = QuantityComponent(value=10, unit=metric.meter)
    seconds = FundamentalTimeUnit(name="second", symbol="s", power=-2)
    ten_seconds = QuantityComponent(value=10, unit=seconds)
    
    my_unit = Unit.from_quantity_components(ten_meters, ten_seconds)
    print(my_unit)
if __name__ == "__main__":
    main()