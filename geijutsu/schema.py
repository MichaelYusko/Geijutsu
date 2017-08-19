import abc

# TODO Add Int, Boolean, Array, Float classes


class Field(metaclass=abc.ABCMeta):
    """Base interface for the all type classes

    Methods:
        validate  Validate an dict object
    """
    @abc.abstractmethod
    def validate(self, data):
        pass


class Str(Field):
    """Validation class for string values

      Attributes:
          max_length Validate length of string
    """

    # TODO add min_length/regex and etc attributes
    # TODO add custom errors into an array
    # TODO refactor the class;)

    def __init__(self, max_length=None, min_length=None):
        self.max_length = max_length
        self.min_length = min_length

    errors = {
        'max_length': 'max_len',
        'min_length': 'min_len'
    }

    def validate(self, data):
        for key, value in data.items():
            errors = []
            if len(value) >= self.__dict__['max_length']:
                errors.append(self.errors['max_length'])
                data[key] = errors

            if len(value) <= self.__dict__['min_length']:
                errors.append(self.errors['min_length'])
                data[key] = errors
        return data


class BaseSchema:
    """Base class for type classes

        Methods:
            validate Validate an dict object, or return dict an object with errors

        Attributes:
            data an dict object with data
    """

    # TODO ?
    # TODO refactor the class;)

    def __new__(cls, *args, **kwargs):
        value = cls.__dict__['properties']
        k = value['name']
        print(k.validate(args[0]))
