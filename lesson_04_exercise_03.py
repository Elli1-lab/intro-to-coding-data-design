colors = []

for i in range(5):
    color = input(f"Enter your favorite colour: ")
    colors.append(color)

    print("Your favorite colours are: " + ", " .join(colors))