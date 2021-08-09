import requests
from forecast import Forecast
def getForecastFromZip (zipCode):
    url = f"http://api.openweathermap.org/data/2.5/weather?zip={zipCode}&units=imperial&appid=4ca3a90bd6f46affe15060d50fadf9e6"
    response = requests.get (url)
    weatherData = response.json ()
    forecast = Forecast (weatherData)
    return forecast
print ("Welcome to Becky's Weather")
zipCode = input ("Enter zip code ")
forecast = getForecastFromZip (zipCode)
if forecast.status == 200:
    finalWeather = f"{forecast.city} is {forecast.main.temperature} degrees outside with {forecast.condition.description}"
    print (finalWeather)
else:
    print ("Error occurred ")