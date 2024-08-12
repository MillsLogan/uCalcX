from .mass_unit import FundamentalMassUnit

class ImperialMassUnit(FundamentalMassUnit):
    def __init__(self, name: str, symbol: str, ounces_per_unit: float):
        super().__init__(name=name, symbol=symbol)
        self.ounces_per_unit = ounces_per_unit

    def grams_per_unit(self) -> float:
        return self.ounces_per_unit * 28.3495
    
    def _conversion_method(self, other: "ImperialMassUnit", value: float) -> float:
        if not isinstance(other, ImperialMassUnit):
            raise ValueError(f"Tried to convert {self} to {other}. Expected two mass units.")
                
        return value * self.ounces_per_unit / other.ounces_per_unit
    

ounce = oz = ImperialMassUnit(name="ounce", symbol="oz", ounces_per_unit=1)
pound = lb = ImperialMassUnit(name="pound", symbol="lb", ounces_per_unit=16)
stone = st = ImperialMassUnit(name="stone", symbol="st.", ounces_per_unit=224)
short_ton = tn = ImperialMassUnit(name="short ton", symbol="short ton", ounces_per_unit=32000)
long_ton = LT = ImperialMassUnit(name="long ton", symbol="long ton", ounces_per_unit=35840)
slug = ImperialMassUnit(name="slug", symbol="slug", ounces_per_unit=514.785)


