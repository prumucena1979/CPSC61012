# analytics.py

from .record import TemperatureRecord
from .converter import convert # Changed import name

# This function calculates the overall average temperature (in Celsius) across all readings from all records.
# It assumes that for a combined average, comparing in Celsius is appropriate.
def average_temperature_across_days(records: list[TemperatureRecord]) -> float:
    all_readings_celsius = []
    # Return 0.0 for an empty list of records
    if not records:
        return 0.0

    for record in records:
        # Skip invalid records or records with no readings
        if not isinstance(record, TemperatureRecord) or not record.readings:
            continue

        current_scale = record.scale

        # Convert all readings of the current record to Celsius and add to the combined list
        for temp_val in record.readings:
            temp_celsius = convert(temp_val, current_scale, 'celsius') # Use convert
            all_readings_celsius.append(temp_celsius)

    # Return 0.0 if no valid readings were found across all records
    if not all_readings_celsius:
        return 0.0

    # Calculate and return the average, rounded to two decimal places
    return round(sum(all_readings_celsius) / len(all_readings_celsius), 2)

# This function finds the date of the day with the highest average temperature across all records.
# Comparison is done based on the average temperature converted to Celsius.
def hottest_day(records: list[TemperatureRecord]) -> str | None:
    # Return None if the list of records is empty
    if not records:
        return None

    max_avg_temp_celsius = -float('inf') # Initialize with a very low value
    hottest_date = None

    for record in records:
        # Skip invalid records or records with no readings
        if not isinstance(record, TemperatureRecord) or not record.readings:
            continue

        # Get the summary which contains the average in the record's original scale
        summary = record.get_summary()
        # Ensure summary is valid and has the necessary keys
        if not summary or 'avg' not in summary or 'date' not in summary:
            continue

        # Convert the daily average temperature to Celsius for consistent comparison
        avg_temp_original_scale = summary['avg']
        original_scale = record.scale
        avg_temp_celsius = convert(avg_temp_original_scale, original_scale, 'celsius') # Use convert

        # Compare with the current maximum average temperature
        if avg_temp_celsius > max_avg_temp_celsius:
            max_avg_temp_celsius = avg_temp_celsius
            hottest_date = summary['date'] # Store the date of the hottest day

    # hottest_date will remain None if no valid records were processed, which is appropriate
    return hottest_date

# This function returns a list of dates where at least one reading on that day exceeds the given threshold.
# The threshold is assumed to be in Celsius for comparison purposes, so readings are converted.
def detect_extreme_days(records: list[TemperatureRecord], threshold: float) -> list[str]:
    extreme_dates = []
    # Return an empty list if the list of records is empty
    if not records:
        return []

    for record in records:
        # Skip invalid records
        if not isinstance(record, TemperatureRecord) or not hasattr(record, 'date') or not hasattr(record, 'readings') or not hasattr(record, 'scale'):
            continue

        original_readings = record.readings
        original_scale = record.scale
        date = record.date

        # Check if any reading on this day is above the threshold
        is_extreme = False
        for temp in original_readings:
            # Convert each reading to Celsius for comparison with the threshold (in Celsius)
            temp_celsius = convert(temp, original_scale, 'celsius') # Use convert
            if temp_celsius > threshold:
                is_extreme = True
                break # Found one extreme reading, no need to check others for this day

        # Add the date to the list if an extreme reading was found, ensuring no duplicates
        if is_extreme and date not in extreme_dates:
            extreme_dates.append(date)

    return extreme_dates # Return the list of dates

# This function returns a dictionary mapping each date to its (min, max) temperature range.
# The min and max temperatures are returned in their original scale as stored in the record.
def temperature_range_for_each_day(records: list[TemperatureRecord]) -> dict:
    daily_ranges = {}
    # Return an empty dictionary if the list of records is empty
    if not records:
        return {}

    for record in records:
        # Skip invalid records or records with no readings
        if not isinstance(record, TemperatureRecord) or not record.readings:
            continue
        # Get the summary which already provides min/max in the original scale
        summary = record.get_summary()
        # Ensure summary is valid and has date, min, and max
        if not summary or 'date' not in summary or 'min' not in summary or 'max' not in summary:
            continue
        # Map the date to the (min, max) tuple
        daily_ranges[summary['date']] = (summary['min'], summary['max'])

    return daily_ranges # Return the dictionary

# This function analyzes a list of temperature readings and returns a list indicating the trend
# between consecutive readings ('up', 'down', or 'same').
def temperature_trend(temps: list[float]) -> list[str]:
    # Return an empty list if there are fewer than 2 readings
    if len(temps) < 2:
        return []

    trends = []
    # Iterate through the list starting from the second element
    for i in range(1, len(temps)):
        if temps[i] > temps[i - 1]:
            trends.append('up')
        elif temps[i] < temps[i - 1]:
            trends.append('down')
        else:
            trends.append('same')
    return trends # Return the list of trends

# This function checks if there is a significant jump or drop between any two consecutive temperatures
# in a list of readings, defined by a threshold. The threshold defaults to 5.0 degrees.
def detect_spike(temps: list[float], *, threshold: float = 5.0) -> bool:
    # A spike requires at least two readings
    if len(temps) < 2:
        return False

    # Iterate through consecutive pairs of readings
    for i in range(1, len(temps)):
        # Check the absolute difference between the current and previous reading
        if abs(temps[i] - temps[i - 1]) >= threshold:
            return True # Found a spike, return True immediately

    # No spike found if the loop completes without returning True
    return False