from . import imperial, apothecary, metric, molecular
from .mass_unit import MassUnit


__all__ = ["MassUnit", "imperial", "apothecary", "metric", "molecular"]


def get_all_units():
    import inspect
    all_units = []
    all_units.extend(inspect.getmembers(metric, lambda x: inspect.isclass(x) and issubclass(x, MassUnit) and x != MassUnit))
    all_units.extend(inspect.getmembers(imperial, lambda x: inspect.isclass(x) and issubclass(x, MassUnit) and x != MassUnit))
    all_units.extend(inspect.getmembers(apothecary, lambda x: inspect.isclass(x) and issubclass(x, MassUnit) and x != MassUnit))
    all_units.extend(inspect.getmembers(molecular, lambda x: inspect.isclass(x) and issubclass(x, MassUnit) and x != MassUnit))
    return list(map(lambda x: x[1], all_units))
