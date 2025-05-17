# converter.py

# This function converts temperature values between Celsius, Fahrenheit, and Kelvin
# Renamed from convert_temperature to convert as per rubric
def convert(value: float, from_unit: str, to_unit: str) -> float:
    from_unit = from_unit.lower()
    to_unit = to_unit.lower()

    # If converting to the same unit, return the value rounded
    if from_unit == to_unit:
        return round(value, 2)

    # Step 1: Convert the value to Celsius first
    if from_unit == "celsius":
        celsius_temp = float(value)
    elif from_unit == "fahrenheit":
        celsius_temp = (float(value) - 32) * 5/9
    elif from_unit == "kelvin":
        celsius_temp = float(value) - 273.15
    else:
        # Raise error for unknown input unit
        raise ValueError(f"Unsupported 'from_unit': {from_unit}. Must be 'celsius', 'fahrenheit', or 'kelvin'.")

    # Step 2: Convert from Celsius to the desired target unit
    if to_unit == "celsius":
        result = celsius_temp
    elif to_unit == "fahrenheit":
        result = (celsius_temp * 9/5) + 32
    elif to_unit == "kelvin":
        result = celsius_temp + 273.15
    else:
        # Raise error for unknown output unit
        raise ValueError(f"Unsupported 'to_unit': {to_unit}. Must be 'celsius', 'fahrenheit', or 'kelvin'.")

    # Return the final result rounded to two decimal places
    return round(result, 2)