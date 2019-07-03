from weatherinterfaces import Subject, Observer

class WeatherData(Subject):
    def __init__(self):
        self.observers = []
        self.temp = None
        self.pressure = None
        self.humidity = None

    def register_observer(self, o: Observer):
        self.observers.append(o)

    def remove_observer(self, o: Observer):
        self.observers.remove(o)

    def notify_observers(self):
        for observer in self.observers:
            observer.update(self.temp, self.humidity, self.pressure)

    def measurements_changed(self):
        self.notify_observers()

    def set_measurements(self, temp, humidity, pressure):
        self.temp = temp
        self.humidity = humidity
        self.pressure = pressure
        self.measurements_changed()
