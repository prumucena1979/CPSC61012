# CPSC61012
PythonTerm3
# Temperature Analysis Toolkit (`temperature_toolkit`)

This repository contains a simple Python package designed to model, store, convert, and analyze daily temperature readings. It was developed as a project for a Master's course in Data Analytics.

## Project Description

The `temperature_toolkit` package provides tools to handle temperature data across different days and scales. It allows users to:

* Record temperature readings for specific dates.
* Convert temperatures between Celsius, Fahrenheit, and Kelvin.
* Compute summaries such as minimum, maximum, and average temperatures for a day.
* Perform basic analysis across multiple days, like finding the hottest day or detecting extreme temperatures and trends.

## Project Structure

The project is organized as a Python package.

Okay, here is the final version of the README with your repository URL included.

Markdown

# Temperature Analysis Toolkit (`temperature_toolkit`)

This repository contains a simple Python package designed to model, store, convert, and analyze daily temperature readings. It was developed as a project for a Master's course in Data Analytics.

## Project Description

The `temperature_toolkit` package provides tools to handle temperature data across different days and scales. It allows users to:

* Record temperature readings for specific dates.
* Convert temperatures between Celsius, Fahrenheit, and Kelvin.
* Compute summaries such as minimum, maximum, and average temperatures for a day.
* Perform basic analysis across multiple days, like finding the hottest day or detecting extreme temperatures and trends.

## Project Structure

The project is organized as a Python package.

temperature_toolkit/
├── init.py
├── record.py
├── converter.py
├── analytics.py
└── main.py



* `temperature_toolkit/`: This is the main package directory.
* `__init__.py`: Initializes the `temperature_toolkit` directory as a Python package and makes key components available for import.
* `record.py`: Contains the `TemperatureRecord` class, which holds the date, temperature readings for that day, and the scale of the readings. It includes methods for getting summaries, converting scales, and checking thresholds.
* `converter.py`: Holds a utility function (`convert`) for converting a single temperature value between different units.
* `analytics.py`: Contains functions for performing various analytical tasks on one or more `TemperatureRecord` objects, such as calculating averages, finding extreme values, and detecting trends.
* `main.py`: A script outside the package (usually in the root directory of the repo, alongside the `temperature_toolkit` folder) that demonstrates how to use the classes and functions within the `temperature_toolkit` package. It includes example usage and test cases.

## How to Use

1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/prumucena1979/CPSC61012.git](https://github.com/prumucena1979/CPSC61012.git)
    cd CPSC61012
    ```

2.  **Running the Example (`main.py`):**
    The `main.py` script demonstrates the core functionalities of the package. You can run it from the root directory of the repository (after cloning and navigating into the `CPSC61012` folder):
    ```bash
    python main.py
    ```
    This script creates sample `TemperatureRecord` objects, performs conversions and analysis, and prints the results to the console.

3.  **Using the Package in Your Own Script:**
    You can import and use the classes and functions from the `temperature_toolkit` package in your own Python scripts. Make sure your script can access the `temperature_toolkit` directory (e.g., by being in the same parent directory as the `temperature_toolkit` folder).

    ```python
    # Example of how to import and use
    from temperature_toolkit import TemperatureRecord, convert, average_temperature_across_days

    # Create a temperature record
    day1_temps = TemperatureRecord(date="2025-01-01", readings=[20.5, 22.1, 19.8], scale="celsius")

    # Get summary
    print(day1_temps.get_summary())

    # Convert scales
    day1_temps.convert_to("fahrenheit")
    print(day1_temps.get_summary())

    # Use analytics function
    all_records = [day1_temps, ...] # Add other records
    overall_avg = average_temperature_across_days(all_records)
    print(f"Overall average temperature: {overall_avg}°C")
    ```

## Key Functionalities

* **`TemperatureRecord` Class:**
    * Stores daily temperature readings and scale.
    * `convert_to(target_scale)`: Converts readings in-place.
    * `get_summary()`: Provides date, scale, min, max, and average.
    * `is_above_threshold(threshold)`: Checks if all readings exceed a threshold.
* **`convert(value, from_unit, to_unit)` Function:**
    * Converts a single temperature value between 'celsius', 'fahrenheit', and 'kelvin'.
* **Analytics Functions:**
    * `average_temperature_across_days(records)`: Calculates the overall average temperature.
    * `hottest_day(records)`: Finds the date with the highest average temperature.
    * `detect_extreme_days(records, threshold)`: Lists dates where any reading exceeds a threshold.
    * `temperature_range_for_each_day(records)`: Returns min/max temperatures for each day.
    * `temperature_trend(temps)`: Shows 'up', 'down', 'same' trend between readings.
    * `detect_spike(temps, threshold=5)`: Detects significant jumps or drops in readings.

## Assignment Context

This package was developed as Part 1 of the Python Data Analysis Problems Assignment for the Master of Data Analytics program at Niagara College.

## Author

Fabio Prumucena - UNF
