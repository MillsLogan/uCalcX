# uCalcX

**uCalcX** is a Python library for handling units of measurement and performing conversions across various physical quantities. The library currently includes support for the length dimension, with modules designed for metric, imperial, nautical, and land measurements. The library is extensible and will support additional physical quantities in the future.

## Features

### Implemented Modules

**1. Common Module**

The `common` module provides foundational classes and enums that are used across the entire library:

- **Measurement**: 
  - Represents a measurement with a value and unit.
  - Provides a `convert_to` method to convert between different units of the same quantity.

- **Unit**: 
  - An abstract class defining the structure for all units.
  - Contains properties like `full_name` and `full_symbol` to get the unit's name and symbol with metric prefixes.

- **MetricPrefix**:
  - An enum defining metric prefixes from `yotta` to `yocto`.
  - Provides methods for converting between prefixes.

- **Quantity**:
  - An enum representing different physical quantities like Length, Time, Mass, etc.
  - Each quantity has a standard symbol and name.

**2. Length Module**

The `length` module provides implementations for various units of length, organized into submodules for different measurement systems:

- **Metric**: 
  - **Meter**: Represents the meter unit with a base conversion factor of 1.
  - Allows for the application of different metric prefixes like kilometer (km), centimeter (cm), etc.

- **Imperial**: 
  - Provides units used in the US Customary system, including:
    - **Foot**: Represents the foot unit.
    - **Yard**: Represents the yard unit.
    - **Mile**: Represents the mile unit.
    - **Inch**: Represents the inch unit.
    - **Thou (Mil)**: Represents a very small unit used in engineering.
    - **Hand**: Used to measure the height of horses.
    - **Rod, Chain, Furlong**: Additional units for land measurement.

- **Nautical**: 
  - Provides units used in maritime contexts:
    - **Fathom**: Represents the fathom unit.
    - **Nautical Mile**: Represents the nautical mile unit.
    - **Cable**: Represents the cable unit.

- **Land Measurement**: 
  - Includes units commonly used for land measurement:
    - **Rod**: Represents the rod unit.
    - **Chain**: Represents the chain unit.
    - **Furlong**: Represents the furlong unit.

## Usage

As of now, the library supports defining and working with units of length across different measurement systems. You can create instances of various units, apply metric prefixes, and convert between units of the same quantity.

Here is a basic example of how to use the library:

```python
from ucalcx.length.metric import Meter
from ucalcx.length.imperial import Foot
from ucalcx import MetricPrefix, Measurement

# Define the kilometer unit type (A meter prefixed with 'kilo')
kilometer = Meter(MetricPrefix.Kilo)

# Create a foot unit (Defaults to 'Base' prefix)
foot = Foot()

# Define a measurement using the kilometer as the unit
kilometer_measure = Measurement(1, kilometer)

# Convert the measurement to feet
foot_measure = kilometer_measure.convert_to(foot)

print(f"{kilometer_measure} is {value_in_feet} feet, or {value_in_feet.convert_to(Foot(MetricPrefix.Kilo))} kft")
```
**Expected Output:**
```python
1 km is 3280.839895013123 ft or 3.280839895013123 kft
```
## Future Development

Future updates will include:

- **Support for Additional Physical Quantities**: Implementation of modules for Time, Mass, Electric Current, Temperature, Amount of Substance, and Luminous Intensity.
- **Mathematical Operations and Conversions**: Enhanced functionality for performing arithmetic operations and conversions with different units.
- **User Input and Output**: Features to read user input for mathematical operations and output the results.

For detailed implementation and to explore the code, please refer to the source files in the repository.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.