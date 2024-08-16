# uCalcX

**uCalcX** is a Python library for handling units of measurement and performing conversions across various physical quantities. The library includes common base units in each fundamental physical dimension. These units can be combined to make more complex units to handle more complex operations with implicit conversions. UCalcX takes the burden of tracking units and ensuring compatibility off of your shoulders.

## Features
### Fundamental Units
UCalcX provides common units that are used within each physical quantity. For example, the length quantity we provide the `Meter`, `Foot`, `Inch`, and more. The `Meter` class is also able to be altered to handle units that make use of metric prefixes. This can be done like this to make a MegaMeter:

```python
import ucalcx as ucx
from ucalcx.length import Meter # Import the Meter class
kilometer = Meter(ucx.MetricPrefix.Kilo) # Adds the Kilo prefix to the Meter base unit
```

These units can then be added to values using the `Measurement` class. This can be done implicitly using a multiplication operation or by explicitly instantiating the `Measurement` class

```python
# ... imports as above
from ucalcx import Measurement
from ucalcx.length import meter
# Construction using mult operation definition
height_of_box = 5 * meter
# Measurement(value=5, unit=FQUnit(meter, m, FundamentalQuantity.Length))
width_of_box = Measurement(10.2, meter)
# Measurement(value=10.2, unit=FQUnit(kilometer, km, FundamentalQuantity.Length))
```
### Performing Operations and Conversions
UCalcX provides a framework for converting between units that measure the same quantities, as well as performing complex operations with these units to create more complex representations. Using our variables assigned above we can find the area of the box like so,

```python
area_of_box = height_of_box * width_of_box
# Measurement(value=51, unit=Unit(Length))
```

Now we can convert this area to feet like so,
```python
from ucalcx.length.imperial import foot
area_in_sq_ft = area_of_box.convert_to(foot * foot)
# 167.323 ft^2
```

# Future Developments
Creating a shell/input parsing
- Create an interactive shell for the user to type into and perform operations as needed and track units across said operations.
