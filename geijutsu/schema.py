import abc


class Field(metaclass=abc.ABCMeta):
    """Base interface for the all type classes

    Methods:
        validate  Validate an dict object
    """
    @abc.abstractmethod
    def validate(self):
        pass


class Str(Field):
    """Validation class for string values

      Attributes:
          max_length Validate length of string
    """
    def __init__(self, max_length=None):
        self.max_length = max_length

    def validate(self):
        """Validate dict object, and return custom errors if exists"""
        pass


class BaseSchema:
    """Base class for type classes

        Methods:
            validate Validate an dict object, or return dict an object with errors

        Attributes:
            data an dict object with data
    """
    def _validate(self):
        """Validate dict object, and return errors if exists"""
        print(self.data)

    def __init__(self, data):
        self.data = data
