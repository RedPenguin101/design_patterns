class WeatherData:

    def measurementsChanged(self):
        temp = getTemparature()
        humidity = getHumidity()
        pressure = getPressure()

        self.currentConditionsDisplay.update(temp, humidity, pressure)
        self.statisticsDisplay.update(temp, humidity, pressure)
        self.forecastDisplay.update(temp, humidity, pressure)

    # other methods

```
problems: 
    rows 8-10 are areas of change, need to encapsulate
    same rows are coding to concrete implementations
    we are at least using a common interface
    
```
