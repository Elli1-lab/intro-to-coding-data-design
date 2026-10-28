# Ask the user for the city names
city1 = input("Enter the name of the first city:")
city2 = input("Enter the name of the second city:")

# Ask the user for the current temperatures in Celsius
temp1_f = input(f"Please enter the current temperature for {city1} in Fahrenheit: ")
temp2_f = input(f"Please enter the current temperature for {city2} in Fahrenheit: ")

# Convert the temperatures to float
temp1_f = float(temp1_f)
temp2_f = float(temp2_f)

# Convert the temperature to Celsius
temp1_c = (temp1_f - 32) * 5/9
temp2_c = (temp2_f - 32) * 5/9

# Check if the temperature is below freezing point
if temp1_f < 32 and temp2_f < 32:
    print("Alert: Alert: The temperatures in both cities are below freezing point.")
elif temp1_f < 32 or temp2_f <32:
    print("Alert: The temperature in one of the cities is below freezing point.")
else:
    print("The temperatures in both cities are above the freezing point.")

# Print the user input in a formatted string
print(f"The current temperature in {city1} is {temp1_c:.1f} degrees Celsius.")
print(f"The current temperature in {city2} is {temp2_c:.2f} degrees Celsius.")