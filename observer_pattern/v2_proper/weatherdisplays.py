from weatherinterfaces import Observer, Display, Subject


class CurrentConditionsDisplay(Observer, Display):
    def __init__(self, weatherData: Subject):
        self.weatherData = weatherData
        self.weatherData.register_observer(self)
        self.temp = None
        self.humidity = None

    def update(self, temp, humidity, pressure):
        self.temp = temp
        self.humidity = humidity
        self.display()

    def display(self):
        print(
            f"Current conditions: {self.temp} F degrees and "
            f"{self.humidity} humidity"
        )
