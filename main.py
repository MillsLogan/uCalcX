import ucalcx as ucx
from ucalcx import Measurement
from ucalcx import Unit
from ucalcx.mass import kilogram, gram


def main():
    import ucalcx as ucx
    from ucalcx.length import Meter # Import the Meter class
    kilometer = Meter(ucx.MetricPrefix.Kilo) # Adds the Kilo prefix to the Meter base unit
    # ... imports as above
    from ucalcx import Measurement
    from ucalcx.length import meter
    # Construction using mult operation definition
    height_of_box = 5 * meter
    print(height_of_box)
    # Measurement(value=5, unit=FQUnit(meter, m, FundamentalQuantity.Length))
    width_of_box = Measurement(10.2, meter)
    print(width_of_box)
    # Measurement(value=10.2, unit=FQUnit(kilometer, km, FundamentalQuantity.Length))
    area_of_box = height_of_box * width_of_box
    print(area_of_box)
    from ucalcx.length.imperial import foot
    area_in_sq_ft = area_of_box.convert_to(foot * foot)
    print(area_in_sq_ft)
    
    
if __name__ == "__main__":
    main()