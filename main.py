#!/usr/bin/python3
import sys
import os

# This adds the parent directory of the current script to the system path.
# This allows us to import modules from the 'temperature_toolkit' package
# when running this script directly from the command line, even if the
# package is not installed in the standard Python site-packages.
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import main classes and functions from the package
from temperature_toolkit import (
    TemperatureRecord,
    convert, # Changed import name
    average_temperature_across_days,
    hottest_day,
    detect_extreme_days,
    temperature_range_for_each_day,
    temperature_trend,
    detect_spike
)

def main():
    # Create sample TemperatureRecord objects using different temperature scales
    record1 = TemperatureRecord(date="2024-05-01", readings=[10.0, 12.5, 15.0], scale="celsius")
    record2 = TemperatureRecord(date="2024-05-02", readings=[50.0, 53.6, 57.2], scale="fahrenheit")
    record3 = TemperatureRecord(date="2024-05-03", readings=[283.15, 285.15, 287.15], scale="kelvin") # Equivalent to 10, 12, 14 C approx
    record4 = TemperatureRecord(date="2024-05-04", readings=[], scale="celsius")  # Test case: Empty readings
    record5 = TemperatureRecord(date="2024-05-05", readings=[25.0, 25.0, 25.0], scale="celsius") # Test case: Constant temperature
    record6 = TemperatureRecord(date="2024-05-06", readings=[70.0, 75.0, 80.0], scale="fahrenheit") # approx 21-27 C

    print("--- Testing TemperatureRecord Class ---")
    # Test get_summary()
    print(f"Record 1 Summary (Celsius): {record1.get_summary()}")

    # Test convert_to() method
    record1.convert_to("fahrenheit")  # Changed method name
    print(f"Record 1 Converted to Fahrenheit: {record1.get_summary()}")
    record1.convert_to("kelvin")  # Changed method name
    print(f"Record 1 Converted to Kelvin: {record1.get_summary()}")
    record1.convert_to("celsius")  # Changed method name (convert back)
    print(f"Record 1 Converted back to Celsius: {record1.get_summary()}")

    # Test is_above_threshold() method
    print(f"Is Record 1 (Celsius) above 10°C? {record1.is_above_threshold(10)}") # Should be True (all readings > 10)
    print(f"Is Record 1 (Celsius) above 15°C? {record1.is_above_threshold(15)}") # Should be False (10.0, 12.5, 15.0 are not all > 15)
    print(f"Is Record 4 (empty) above 0°C? {record4.is_above_threshold(0)}") # Should be False


    print("\n--- Testing convert Function ---") # Updated function name header
    # Test convert() function directly
    print(f"100 Celsius to Fahrenheit: {convert(100, 'celsius', 'fahrenheit')}") # Updated function name
    print(f"32 Fahrenheit to Celsius: {convert(32, 'fahrenheit', 'celsius')}") # Updated function name
    print(f"0 Celsius to Kelvin: {convert(0, 'celsius', 'kelvin')}") # Updated function name
    print(f"273.15 Kelvin to Celsius: {convert(273.15, 'kelvin', 'celsius')}") # Updated function name
    print(f"100 Fahrenheit to Kelvin: {convert(100, 'fahrenheit', 'kelvin')}") # Updated function name
    print(f"300 Kelvin to Fahrenheit: {convert(300, 'kelvin', 'fahrenheit')}") # Updated function name
    # Added test for same unit conversion
    print(f"25 Celsius to Celsius: {convert(25, 'celsius', 'celsius')}")


    print("\n--- Testing Analysis Functions ---")
    # Create a list of records for analysis functions
    # (Using the records created initially, including the empty one and new record6)
    all_records_for_analysis = [record1, record2, record3, record4, record5, record6]

    # Test average_temperature_across_days()
    print(f"Average temperature across all days (Celsius): {average_temperature_across_days(all_records_for_analysis)}")

    # Test hottest_day()
    print(f"Hottest day: {hottest_day(all_records_for_analysis)}")

    # Test detect_extreme_days() with different thresholds
    print(f"Days with temperatures above 15°C: {detect_extreme_days(all_records_for_analysis, 15)}")
    print(f"Days with temperatures above 25°C: {detect_extreme_days(all_records_for_analysis, 25)}")
    print(f"Days with temperatures above 100°C: {detect_extreme_days(all_records_for_analysis, 100)}") # Test with a high threshold

    # Test temperature_range_for_each_day()
    print(f"Temperature ranges for each day: {temperature_range_for_each_day(all_records_for_analysis)}")

    # Test temperature_trend()
    temps_for_trend = [10.0, 12.5, 11.5, 15.0, 15.0, 14.0]
    print(f"Temperature trend for {temps_for_trend}: {temperature_trend(temps_for_trend)}")
    print(f"Temperature trend for []: {temperature_trend([])}") # Test empty list
    print(f"Temperature trend for [20]: {temperature_trend([20])}") # Test single element list

    # Test detect_spike() with different thresholds and lists
    temps_for_spike_true = [10, 12, 11, 18, 19, 20] # Spike between 11 and 18 (diff 7)
    print(f"Spike detected in {temps_for_spike_true} (default threshold 5): {detect_spike(temps_for_spike_true)}") # Should be True
    print(f"Spike detected in {temps_for_spike_true} (threshold 3): {detect_spike(temps_for_spike_true, threshold=3)}") # Should be True
    print(f"Spike detected in {temps_for_spike_true} (threshold 10): {detect_spike(temps_for_spike_true, threshold=10)}") # Should be False

    temps_for_spike_false = [10, 12, 11, 13, 14, 15] # Max diff is 2
    print(f"Spike detected in {temps_for_spike_false} (threshold=5): {detect_spike(temps_for_spike_false, threshold=5)}") # Should be False

    # Test edge cases for detect_spike
    print(f"Spike detected in empty list: {detect_spike([])}") # Should be False
    print(f"Spike detected in list with one element: {detect_spike([10])}") # Should be False
    # Added test for spike exactly on the threshold
    temps_for_spike_exact = [10, 15] # Diff is 5
    print(f"Spike detected in {temps_for_spike_exact} (threshold=5): {detect_spike(temps_for_spike_exact, threshold=5)}") # Should be True


    print("\n--- Testing TemperatureRecord with empty readings ---")
    # Test how methods handle records with empty readings
    record_empty_readings = TemperatureRecord(date="2024-05-07", readings=[], scale="celsius")
    print(f"Summary for record with empty readings: {record_empty_readings.get_summary()}") # Should show 0s for min/max/avg
    print(f"Is record with empty readings above 20°C? {record_empty_readings.is_above_threshold(20)}") # Should be False
    record_empty_readings.convert_to("fahrenheit") # Test conversion on empty readings
    print(f"Summary for record with empty readings after conversion: {record_empty_readings.get_summary()}") # Should still show 0s and updated scale


if __name__ == "__main__":
    main()