"""Module for length units commonly used in land measurement and surveying.

This module contains classes for units of length used in land measurement and surveying, 
including the chain, rod, furlong, and league. These units are part of the imperial system 
and are used to measure distances in land-based contexts.

All units in this module are subclasses of the `ImperialLengthUnit` class, which provides
a common interface for working with imperial length units. The `ImperialLengthUnit` class
defines the conversion to the inch unit, which is then converted to the meter unit for
consistency across different systems.

For more information about land measurement units and their history, refer to the following resources:
- [Chain on Wikipedia](https://en.wikipedia.org/wiki/Chain_(unit))
- [Rod on Wikipedia](https://en.wikipedia.org/wiki/Rod_(unit))
- [Furlong on Wikipedia](https://en.wikipedia.org/wiki/Furlong)
- [League on Wikipedia](https://en.wikipedia.org/wiki/League_(unit))

Example:
    All units in this module can be imported and used individually. For example, to use the `Chain` class:

    >>> from ucalcx.length.land import Chain
    >>> chain = Chain()
    >>> print(chain)
    chain (ch)
"""

from .imperial import ImperialLengthUnit


class Chain(ImperialLengthUnit):
    """A class representing the chain unit of length in the imperial system.

    The chain is a unit of length used in land measurement and surveying. It is equal to 66 feet or 792 inches.

    - **Name**: "chain"
    - **Symbol**: "ch"
    - **Inches per Unit**: 792.0

    More information about the chain unit can be found in the following resource:
    - [Chain on Wikipedia](https://en.wikipedia.org/wiki/Chain_(unit))
    """

    name: str = "chain"
    symbol: str = "ch"
    inches_per_unit: float = 792.0


class Rod(ImperialLengthUnit):
    """A class representing the rod unit of length in the imperial system.

    The rod is a unit of length used in land measurement and surveying. It is equal to 16.5 feet or 198 inches.

    - **Name**: "rod"
    - **Symbol**: "rd"
    - **Inches per Unit**: 198.0

    More information about the rod unit can be found in the following resource:
    - [Rod on Wikipedia](https://en.wikipedia.org/wiki/Rod_(unit))
    """

    name: str = "rod"
    symbol: str = "rd"
    inches_per_unit: float = 198.0


class Perch(Rod):
    """A class representing the perch unit of length in the imperial system.
    
    The perch is a unit of length used in land measurement and surveying. It is equal to 5.5 yards or 16.5 feet.
    It is also known as a rod or pole.

    - **Name**: "perch"
    - **Symbol**: "P"
    - **Inches per Unit**: 198.0

    More information about the perch unit can be found in the following resource:
    - [Perch on Wikipedia](https://en.wikipedia.org/wiki/Perch_(unit))
    """

    name: str = "perch"
    symbol: str = "P"


class Pole(Rod):
    """A class representing the pole unit of length in the imperial system.

    The pole is a unit of length used in land measurement and surveying. It is equal to 5.5 yards or 16.5 feet.
    It is also known as a rod or perch.

    - **Name**: "pole"
    - **Symbol**: "P"
    - **Inches per Unit**: 198.0

    More information about the pole unit can be found in the following resource:
    - [Pole on Wikipedia](https://en.wikipedia.org/wiki/Pole_(unit))
    """

    name: str = "pole"
    symbol: str = "P"


class Furlong(ImperialLengthUnit):
    """A class representing the furlong unit of length in the imperial system.

    The furlong is a unit of length used in land measurement and surveying. It is equal to 220 yards or 660 feet.

    - **Name**: "furlong"
    - **Symbol**: "fur"
    - **Inches per Unit**: 7920.0

    More information about the furlong unit can be found in the following resource:
    - [Furlong on Wikipedia](https://en.wikipedia.org/wiki/Furlong)
    """

    name: str = "furlong"
    symbol: str = "fur"
    inches_per_unit: float = 7920.0


class Link(ImperialLengthUnit):
    """A class representing the link unit of length in the imperial system.
    
    The link is a unit of length used in land measurement and surveying. It is equal to 7.92 inches.

    - **Name**: "link"
    - **Symbol**: "li"
    - **Inches per Unit**: 7.92

    More information about the link unit can be found in the following resource:
    - [Link on Wikipedia](https://en.wikipedia.org/wiki/Link_(unit))
    """

    name: str = "link"
    symbol: str = "li"
    inches_per_unit: float = 7.92
    

class League(ImperialLengthUnit):
    """A class representing the league unit of length in the imperial system.
    
    The league is a unit of length used in land measurement and surveying. It is equal to 3 miles or 15840 feet.
    
    - **Name**: "league"
    - **Symbol**: "leag"
    - **Inches per Unit**: 190080.0

    More information about the league unit can be found in the following resource:
    - [League on Wikipedia](https://en.wikipedia.org/wiki/League_(unit))
    """
    
    name: str = "league"
    symbol: str = "leag"
    inches_per_unit: float = 190080.0
