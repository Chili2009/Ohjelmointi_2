import requests
def get_weather(api_key, city_name):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}"
    response = requests.get(url)

    if response.status_code == 200:
        weather_data = response.json()
        temperature_kelvin = weather_data["main"]["temp"]
        temperature_celsius = temperature_kelvin - 273.15  # Kelvin to Celsius conversion
        weather_description = weather_data["weather"][0]["description"]
        return f"Weather in {city_name}: {weather_description}, Temperature: {temperature_celsius:.2f} °C"
    else:
        return "Unable to fetch weather data."


if __name__ == "__main__":
    api_key = "YOUR_API_KEY_HERE"  # Replace with your OpenWeather API key
    city_name = input("Enter city name: ")

    weather_info = get_weather(api_key, city_name)
    print(weather_info)