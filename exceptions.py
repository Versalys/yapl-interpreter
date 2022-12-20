class SourceLexingException(Exception):
    pass


class RedeclarionError(Exception):
    pass


class UndeclaredError(Exception):
    pass

class TypeMismatchError(Exception):
    pass

class OutOfBoundsError(Exception):
    pass


class CompilerTypeMismatchError(Exception):
    def __init__(self, expect, found, where=None):
        if where:
            self.message=f'Type Mismatch in {where}: expected={expect} found={found}'
        else:
            self.message=f'Type Mismatch: expected={expect} found={found}'
