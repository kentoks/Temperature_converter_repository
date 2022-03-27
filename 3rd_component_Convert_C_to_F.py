"""3rd component, Converting Celsius to Fahrenheit version 1
Going to convert from Celsius to Fahrenheit
Function takes in a value, does the conversion and put answer into a list
"""

def to_fahrenheit(from_celsius):
    fahrenheit = (from_celsius * 9/5) + 32
    return fahrenheit

# Main routine

eg_temperatures = [0, 40 ,100]
converted = []

for item in eg_temperatures:
    answer = to_fahrenheit(item)
    answer_statement = f"{item} degrees C is the same as {answer} degrees F"
    converted.append(answer_statement)

print(converted)
