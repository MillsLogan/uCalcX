

class UCalcXError(Exception):
    """ Base class for all exceptions in UCalcX """
    
    pass


class IncompatibleUnitsError(UCalcXError):
    """ Raised when two units are incompatible for a given operation. """
    
    def __init__(self, message, *args, **kwargs):
        super().__init__(message)


class InvalidOperationError(UCalcXError):
    """ Raised when an invalid operation is attempted. """
    
    def __init__(self, message, *args, **kwargs):
        super().__init__(message)


class InvalidValueError(UCalcXError):
    """ Raised when an invalid value is passed to a function. """
    
    def __init__(self, message, *args, **kwargs):
        super().__init__(message)



class InvalidUnitError(UCalcXError):
    """ Raised when an invalid unit is passed to a function. """
    
    def __init__(self, message, *args, **kwargs):
        super().__init__(message)