# Ask the user for the city name
city = input("Enter the name of a city: ")

# Ask the user for the current temperature in Fahrenheit
temp_f = input("Enter the current temperature in Fahrenheit: ")

# Convert the temperature to float
temp_f = float(temp_f)

# Convert the temperature to Celsius
temp_c = (temp_f - 32) * 5/9

# Check if the temperature is below freezing point
if temp_c < 0:
    print("Alert: The temperature is below freezing point.")
else:
    print("The temperature is above the freezing point.")

# Print the user input in a formatted string
print(f"The current temperature in {city} is {temp_c:.1f} degrees Celsius.")