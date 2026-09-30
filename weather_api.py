import requests

api_key = "YOUR_API_KEY"
city = input("Enter city name: ")

url = "https://api.openweathermap.org/data/2.5/weather"

params = {
    "q": city,
    "appid": api_key,
    "units": "metric"
}

response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()

    temperature = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    weather = data["weather"][0]["description"]

    print("\nWeather Details")
    print("City:", city)
    print("Temperature:", temperature, "°C")
    print("Humidity:", humidity, "%")
    print("Condition:", weather)

else:
    print("City not found or API error")