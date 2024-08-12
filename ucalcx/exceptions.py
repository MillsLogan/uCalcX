

class UCalcXError(Exception):
    pass


class IncompatibleUnitsError(UCalcXError):
    def __init__(self, message, *args, **kwargs):
        super().__init__(message)


class InvalidOperationError(UCalcXError):
    def __init__(self, message, *args, **kwargs):
        super().__init__(message)


class InvalidValueError(UCalcXError):
    def __init__(self, message, *args, **kwargs):
        super().__init__(message)



class InvalidUnitError(UCalcXError):
    def __init__(self, message, *args, **kwargs):
        super().__init__(message)