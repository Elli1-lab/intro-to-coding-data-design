# Ask the user for the city names
city_1 = input("Please enter the name of the first city:")
city_2 = input("Please enter the name of the second city:")

# Ask the user for the current temperatures in Celsius
# Convert the temperatures to float
temperature_1 = float(input(f"Please enter the current temperature for {city_1}:"))
temperature_2 = float(input(f"Please enter the current temperature for {city_2}:"))

# Calculate the average temperature
average_temperature = (temperature_1 + temperature_2) / 2

# Print the user input in a formatted string
print(f"The average temperature between {city_1} and {city_2} is {average_temperature} degrees Celsius.")