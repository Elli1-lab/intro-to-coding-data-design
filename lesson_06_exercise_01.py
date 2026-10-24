import requests


# Dictionary with weather codes
WEATHER_CODES = {
    0: "Clear sky",
    1: "Mainly clear",
    2: "Partly cloudy",
    3: "Overcast",
    45: "Fog",
    48: "Depositing rime fog",
    51: "Light drizzle", 
    53: "Moderate drizzle",
    55: "Dense drizzle",
    56: "Light freezing drizzle",
    57: "Dense freezing drizzle",
    61: "Slight rain",
    63: "Moderate rain",
    65: "Heavy rain",
    66: "Light freezing rain",
    67: "Heavy freezing rain",
    71: "Slight snow fall",
    73: "Moderate snow fall",
    75: "Heavy snow fall",
    77: "Snow grains",
    80: "Slight rain shower",
    81: "Moderate rain shower",
    82: "Violent rain shower",
    85: "Slight snow shower",
    86: "Heavy snow shower",
    95: "Thunderstorm",
    96: "Thunderstorm with slight hail",
    99: "Thunderstorm with heavy hail",
}


# Function to get coordinates
def get_coordinates(city_name):

    url = f"https://geocoding-api.open-meteo.com/v1/search?name={city_name}&count=1&language=en&format=json"

    response = requests.get(url)

    data = response.json()

    if "results" not in data:
        raise Exception("City not found.")

    latitude = data["results"][0]["latitude"]
    longitude = data["results"][0]["longitude"]
    elevation = data["results"][0]["elevation"]

    return latitude, longitude, elevation


# Function to get weather
def get_weather(city_name):

    try:
        latitude, longitude, elevation = get_coordinates(city_name)

    except Exception as e:
        print(e)
        return "Error", float("nan")

    # Create API URL
    url = "https://api.open-meteo.com/v1/forecast?"
    url += "current_weather=true"
    url += f"&latitude={latitude:.2f}"
    url += f"&longitude={longitude:.2f}"
    url += f"&elevation={elevation:.2f}"

    # Send request
    response = requests.get(url)

    # Convert JSON to dictionary
    data = response.json()

    # Get temperature and weather code
    temperature = data["current_weather"]["temperature"]
    weather_code = data["current_weather"]["weathercode"]

    # Get weather description
    weather = WEATHER_CODES.get(weather_code, "Unknown weather")

    return weather, temperature


# Main program
if __name__ == "__main__":

    while True:

        city = input("Please enter the name of a city: ")

        if city.lower() == "exit":
            break

        weather, temperature = get_weather(city)

        if weather == "Error":
            continue

        print(
            f"The current weather in {city} is {weather} "
            f"and the temperature is {temperature}°C."
        )