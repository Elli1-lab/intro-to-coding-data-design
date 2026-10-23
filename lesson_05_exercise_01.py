cities = {}

while True:
    city = input("Please enter the name of a city: ")

    if city.lower() == "exit":
        break

    unit = input(
        "Would you like to enter the temperature in Fahrenheit or Celsius?: "
    ).strip().lower()

    if unit == "celsius":
        celsius = float(input(
            f"Please enter the current temperature in Celsius in {city}: "
        ))
        fahrenheit = (celsius * 9 / 5) + 32

    elif unit == "fahrenheit":
        fahrenheit = float(input(
            f"Please enter the current temperature in Fahrenheit in {city}: "
        ))
        celsius = (fahrenheit - 32) * 5 / 9

    else:
        print("Invalid temperature unit. Please try again.")
        continue

    rain = input(f"Is it raining in {city}? (yes/no): ").strip().lower()
    sun = input(f"Is the sun shining in {city}? (yes/no): ").strip().lower()

    cities[city] = {
        "celsius": celsius,
        "fahrenheit": fahrenheit,
        "rain": rain,
        "sun": sun
    }

    print()

print("\nSummary:")

for city, weather in cities.items():
    celsius = weather["celsius"]
    fahrenheit = weather["fahrenheit"]
    rain = weather["rain"]
    sun = weather["sun"]

    sun_text = "sun" if sun == "yes" else "no sun"
    rain_text = "rain" if rain == "yes" else "no rain"

    print(
        f"{city}: {celsius:.0f}°C, {fahrenheit:.0f}°F, "
        f"{sun_text} and {rain_text}"
    )

    if celsius < 0:
        print(f"Warning: The temperature in {city} is below the freezing point")

    if rain == "yes" and sun == "yes":
        print(f"There is a rainbow in {city}.")

    print()