# record.py

# Import the temperature conversion function
from .converter import convert

class TemperatureRecord:
    def __init__(self, date: str, readings: list[float], scale: str):
        self.date = date
        self.readings = readings
        # Store scale in lowercase for consistency
        self.scale = scale.lower()
        # Basic validation for scale (optional but good practice)
        if self.scale not in ['celsius', 'fahrenheit', 'kelvin']:
             raise ValueError(f"Unsupported scale: {scale}. Must be 'celsius', 'fahrenheit', or 'kelvin'.")


    # This method changes all readings to a different scale (Celsius, Fahrenheit, or Kelvin)
    # Renamed from convert_to_scale to convert_to as per rubric
    def convert_to(self, target_scale: str):
        target_scale = target_scale.lower()

        # If target is the same as current, do nothing
        if self.scale == target_scale:
            return

        # Validate target scale (optional but good practice)
        if target_scale not in ['celsius', 'fahrenheit', 'kelvin']:
             raise ValueError(f"Unsupported target_scale: {target_scale}. Must be 'celsius', 'fahrenheit', or 'kelvin'.")


        converted_readings = []
        # Use the imported convert function for each reading
        for temp in self.readings:
            converted_temp = convert(temp, self.scale, target_scale)
            converted_readings.append(converted_temp)

        # Update the readings and scale of the record
        self.readings = converted_readings
        self.scale = target_scale

    # This method gives a summary of the temperature readings
    def get_summary(self) -> dict:
        # Handle empty readings list gracefully
        if not self.readings:
            avg_temp = 0.0 # Use float 0 for average
            min_temp = 0.0 # Use float 0 for min
            max_temp = 0.0 # Use float 0 for max
        else:
            # Calculate min, max, and average
            avg_temp = round(sum(self.readings) / len(self.readings), 2)
            min_temp = min(self.readings)
            max_temp = max(self.readings)

        # Return dictionary with specified keys
        return {
            'date': self.date,
            'scale': self.scale,
            'min': min_temp,
            'max': max_temp,
            'avg': avg_temp
        }

    # Checks if all readings are above a threshold
    def is_above_threshold(self, threshold: float) -> bool:
        # If there are no readings, it's not true that *all* readings are above the threshold
        if not self.readings:
            return False
        # Use a generator expression with all() for a concise check
        return all(reading > threshold for reading in self.readings)