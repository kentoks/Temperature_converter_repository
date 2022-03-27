"""3rd component, Converting Fahrenheit to Celsius version 1
Going to convert from Fahrenheit to Celsius
Function takes in a value, does the conversion and put answer into a list
"""

def to_celsius(from_fahrenheit):
    celsius = (from_fahrenheit - 32) * 5/9
    return celsius

# Main routine

eg_temperatures = [0, 32 ,100]
converted = []

for item in eg_temperatures:
    answer = to_celsius(item)
    answer_statement = f"{item} degrees F is the same as {answer} degrees C"
    converted.append(answer_statement)

print(converted)
