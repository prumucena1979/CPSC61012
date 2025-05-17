# This file makes the temperature_toolkit directory a Python package.
# It also defines which parts of the package are accessible when using `from temperature_toolkit import *`

from .record import TemperatureRecord
from .converter import convert  # Renamed import
from .analytics import (
    average_temperature_across_days,
    hottest_day,
    detect_extreme_days,
    temperature_range_for_each_day,
    temperature_trend,
    detect_spike
)

__all__ = [
    "TemperatureRecord",
    "convert",  # Changed from convert_temperature
    "average_temperature_across_days",
    "hottest_day",
    "detect_extreme_days",
    "temperature_range_for_each_day",
    "temperature_trend",
    "detect_spike"
]