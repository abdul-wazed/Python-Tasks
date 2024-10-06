# Print message
print("Calculate fuel consumption.")

# Ask for the travel distance and store the input
Feed = input("Enter travel distance(kilometers): ")

# assign Distance
Distance = int(Feed)

# Ask for the fuel usage
Feed = input("Enter fuel usage(liters): ")

# assign FuelUsage
FuelUsage = int(Feed)

# Calculate the fuel consumption for 100 km
Consumption = (FuelUsage / Distance) * 100

# Convert the consumption back to an integer
Consumption = int(Consumption)

print(f"Fuel consumption is {Consumption} l per 100 km.")
