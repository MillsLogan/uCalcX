from .length_unit import FundamentalLengthUnit

class NauticalFundamentalLengthUnit(FundamentalLengthUnit):
    def __init__(self, name: str, symbol: str, meters_per_unit: float):
        super().__init__(name=name, symbol=symbol)
        self._meters_per_unit = meters_per_unit

    def meters_per_unit(self) -> float:
        return self._meters_per_unit
    

fathom = fth = NauticalFundamentalLengthUnit(name="fathom",
                                                symbol="fth",
                                                meters_per_unit=1.8288)

cable = cb = NauticalFundamentalLengthUnit(name="cable",
                                            symbol="cb",
                                            meters_per_unit=185.2)

nautical_mile = nmi = NauticalFundamentalLengthUnit(name="nautical mile",
                                                    symbol="nmi",
                                                    meters_per_unit=1852.0)

league = lea = NauticalFundamentalLengthUnit(name="league",
                                                symbol="lea",
                                                meters_per_unit=5556.0)

