import abc


class Observer(abc.ABC):
    @abc.abstractmethod
    def update(temp, humidity, pressure):
        pass


class Display(abc.ABC):
    @abc.abstractmethod
    def display():
        pass


class Subject(abc.ABC):
    @abc.abstractmethod
    def register_observer(self, o: Observer):
        pass

    @abc.abstractmethod
    def remove_observer(self, o: Observer):
        pass

    @abc.abstractmethod
    def notify_observers(self):
        pass


