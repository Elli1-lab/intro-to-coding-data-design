#1
city = ""
while True:
    city = input("Please enter the name of a city: ")

    # Stop the loop if the user enters "exit"
    if city.lower() == "exit":
            break 

# Ask the user for the current temperature in Fahrenheit
fahrenheit = float(input(f"Please enter the current temperature in Fahrenheit in {city}: "))

# Convert the temperature to Celsius
celsius = (fahrenheit - 32) * 5 / 9

# Print the result in a formated string
print(f"The current temperature in {city} is {fahrenheit:.0f}°F or {celsius:.0f}°C.")

# Check if the temperature is below the freezing  point
if celsius < 0:
    print("Warning: The temperature is below freezing point.")

# Print an empty line to separate the cities
print()    