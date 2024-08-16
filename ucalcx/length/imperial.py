from .length_unit import FundamentalLengthUnit

METERS_PER_INCH = 0.0254

class ImperialFundamentalLengthUnit(FundamentalLengthUnit):
    """ Represents an imperial fundamental length unit. """
    _name: str
    _symbol: str

    def __init__(self, name: str, symbol: str, inches_per_unit: float):
        super().__init__(name=name, symbol=symbol)
        self.inches_per_unit = inches_per_unit

    def meters_per_unit(self) -> float:
        """ Returns the number of meters per unit. """
        
        return self.inches_per_unit * METERS_PER_INCH

    def convert_to(self, other: FundamentalLengthUnit, value: float) -> float:
        """ Convert a value from this unit to another unit."""
        
        if isinstance(other, ImperialFundamentalLengthUnit):
            return value * self.inches_per_unit / other.inches_per_unit
        return super().convert_to(other, value)
    

thou = mil = ImperialFundamentalLengthUnit(name="thou",
                                           symbol="mil",
                                           inches_per_unit=0.001)
""" Thou (mil) - 0.001 inches """

inch = in_ = ImperialFundamentalLengthUnit(name="inch",
                                             symbol="in",
                                             inches_per_unit=1.0)
""" Inch (in) - 1 inch """

hand = hh = ImperialFundamentalLengthUnit(name="hand",
                                            symbol="hh",
                                            inches_per_unit=4.0)
""" Hand (hh) - 4 inches """

foot = ft = ImperialFundamentalLengthUnit(name="foot",
                                            symbol="ft",
                                            inches_per_unit=12.0)
""" Foot (ft) - 12 inches """

yard = yd = ImperialFundamentalLengthUnit(name="yard",
                                            symbol="yd",
                                            inches_per_unit=36.0)
""" Yard (yd) - 36 inches """

mile = mi = ImperialFundamentalLengthUnit(name="mile",
                                            symbol="mi",
                                            inches_per_unit=63360.0)
""" Mile (mi) - 63,360 inches """
