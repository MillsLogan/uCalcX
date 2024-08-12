from common import FundamentalQuantityUnit, FundamentalQuantity
from abc import abstractmethod, ABC

class FundamentalTemperatureUnit(FundamentalQuantityUnit, ABC):
    def __init__(self, name: str, symbol: str):
        super().__init__(name=name, symbol=symbol, quantity=FundamentalQuantity.Temperature)

    def _conversion_method(self, other: "FundamentalTemperatureUnit", value: float) -> float:
        if not isinstance(other, FundamentalTemperatureUnit):
            raise ValueError(f"Tried to convert {self} to {other}. Expected two mass units.")
                
        return other.from_celsius(self.to_celsius(value))

    @abstractmethod
    def to_celsius(self, value: float) -> float:
        pass

    @abstractmethod
    def from_celsius(self, value: float) -> float:
        pass
            

class Celsius(FundamentalTemperatureUnit):
    def __init__(self):
        super().__init__(name="celsius", symbol="°C")

    def to_celsius(self, value: float) -> float:
        return value
    
    def from_celsius(self, value: float) -> float:
        return value


class Fahrenheit(FundamentalTemperatureUnit):
    def __init__(self):
        super().__init__(name="fahrenheit", symbol="°F")

    def to_celsius(self, value: float) -> float:
        return (value - 32) * 5/9
    
    def from_celsius(self, value: float) -> float:
        return value * 9/5 + 32
    

class Kelvin(FundamentalTemperatureUnit):
    def __init__(self):
        super().__init__(name="kelvin", symbol="K")

    def to_celsius_conversion(self, value: float) -> float:
        return value + 273.15
    
    def from_celsius_conversion(self, value: float) -> float:
        return value - 273.15
    
class Rankine(FundamentalTemperatureUnit):
    def __init__(self):
        super().__init__(name="rankine", symbol="°R")

    def to_celsius(self, value: float) -> float:
        return (value - 491.67) * 5/9
    
    def from_celsius(self, value: float) -> float:
        return value * 9/5 + 491.67
    
