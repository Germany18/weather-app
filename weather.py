import requests
print ("Welcome to Becky's Weather")
zipCode = input ("Enter zip code ")
url = f"http://api.openweathermap.org/data/2.5/weather?zip={zipCode}&units=imperial&appid=4ca3a90bd6f46affe15060d50fadf9e6"
response = requests.get (url)
weatherData = response.json ()
status = weatherData ["cod"]
if status == 200:
    city = weatherData ["name"]
    mainData = weatherData ["main"]
    temperature = mainData ["temp"]
    weatherLists = weatherData ["weather"]
    conditionData = weatherLists [0]
    description = conditionData ["description"]
    finalWeather = f"{city} is {temperature} degrees outside with {description}"
    print (finalWeather)
else:
    print ("Error occurred")