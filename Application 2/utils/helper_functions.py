# utils/helper_functions.py

def kelvin_to_celsius(kelvin):
    """Convert temperature from Kelvin to Celsius."""
    return kelvin - 273.15

def check_alert_threshold(temperature, threshold):
    """Check if the temperature exceeds the alert threshold."""
    return temperature > threshold
