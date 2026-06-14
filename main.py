import requests

city = input("Enter city: ")

#API for location
url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1"

response = requests.get(url)
data = response.json()

# check if country exists
if "results" not in data:
    print("City not found")
    exit()

result = data["results"][0]
city_name = result["name"]

latitude = result["latitude"]
longitude = result["longitude"]

#Api for weather
weather_url = (
    f"https://api.open-meteo.com/v1/forecast"
    f"?latitude={latitude}"
    f"&longitude={longitude}"
    f"&current=temperature_2m,relative_humidity_2m,wind_speed_10m"
)

weather_response = requests.get(weather_url)
weather_data = weather_response.json()

current = weather_data["current"]

temperature = current["temperature_2m"]
humidity = current["relative_humidity_2m"]
wind_speed = current["wind_speed_10m"]

with open("weather_report.txt", "w") as file:
    file.write("Weather Report\n")
    file.write("----------------\n")
    file.write(f"City: {city_name}\n")
    file.write(f"Temperature: {temperature} °C\n")
    file.write(f"Humidity: {humidity} %\n")
    file.write(f"Wind Speed: {wind_speed} km/h\n")

print("File saves successfully!")