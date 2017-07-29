import abc


class HTTPViews(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get(self):
        pass

    @abc.abstractmethod
    def post(self):
        pass

    @abc.abstractmethod
    def patch(self):
        pass

    @abc.abstractmethod
    def delete(self):
        pass


class UserViews(HTTPViews):
    def patch(self):
        pass

    def post(self):
        pass

    def delete(self):
        pass

    def get(self):
        return 'hello'
