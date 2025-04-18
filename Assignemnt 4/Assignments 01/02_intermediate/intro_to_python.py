# Get the numeric value since input() returns a value in string form
earth_weight = float(earth_weight_str)

# Having a variable for each piece of information is a good habit
mars_weight = earth_weight * MARS_MULTIPLE
rounded_mars_weight = round(mars_weight, 2)


# Note the string concatenation!
print('The equivalent weight on Mars: ' + str(rounded_mars_weight))

# Prompt the user for the name of a planet
planet = input("Enter a planet: ")

# Determine the gravitational constant for the selected planet
if planet == "Mercury":
    gravity_constant = MERCURY_GRAVITY
elif planet == "Venus":
    gravity_constant = VENUS_GRAVITY
elif planet == "Mars":
    gravity_constant = MARS_GRAVITY
elif planet == "Jupiter":
    gravity_constant = JUPITER_GRAVITY
elif planet == "Saturn":
    gravity_constant = SATURN_GRAVITY
elif planet == "Uranus":
    gravity_constant = URANUS_GRAVITY
else:
    # can assume user types in one of these planets, so this can be an else instead of elif
    gravity_constant = NEPTUNE_GRAVITY

# Calculate the equivalent weight on the selected planet
planetary_weight = earth_weight * gravity_constant
rounded_planetary_weight = round(planetary_weight, 2)

# Print the result
print("The equivalent weight on " + planet + ":  " + str(rounded_planetary_weight))