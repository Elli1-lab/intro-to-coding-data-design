# Init variables for the highest and lowest temperatures and the corresponding city names
highest_temp = None
highest_city = None
lowest_temp = None
lowest_city = None

while True:
    city = input("Please enter the name of a city: ")
# Stop the loop if the user enters exit
    if city.lower() == "exit":
        break

    # Ask for the temperature in Fahrenheit
    fahrenheit = float( input(f"Please enter the current temperature in Fahrenheit in {city}: "))

    # Convert Fahrenheit to Celsius
    celsius = (fahrenheit - 32) * 5 / 9

    # Print the current temperatures
    print(
        f"The current temperature in {city} is "
        f"{fahrenheit:.0f}°F or {celsius:.1f}°C.")

    # Check if the temperature is below freezing point
    if fahrenheit < 32:
        print("Warning: The temperature is below freezing point.")

    # Save the first temperature
    if highest_celsius is None:
        highest_celsius = celsius
        lowest_celsius = celsius
        highest_city = city
        lowest_city = city

    # Check for a new highest temperature
    elif celsius > highest_celsius:
        highest_celsius = celsius
        highest_city = city

    # Check for a new lowest temperature
    elif celsius < lowest_celsius:
        lowest_celsius = celsius
        lowest_city = city

    print()

# Print the summary
if highest_celsius is not None:
    print("Summary:")
    print(
        f"The highest temperature is {highest_celsius:.1f}°C "
        f"in {highest_city}." )
    print(
        f"The lowest temperature is {lowest_celsius:.1f}°C "
        f"in {lowest_city}." )
else:
    print("No cities were entered.")
