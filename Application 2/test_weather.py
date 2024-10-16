# test_weather.py

import unittest
from utils.helper_functions import kelvin_to_celsius, check_alert_threshold

class TestWeatherProcessing(unittest.TestCase):
    
    def test_kelvin_to_celsius(self):
        self.assertEqual(round(kelvin_to_celsius(300), 2), 26.85)
    
    def test_check_alert_threshold(self):
        self.assertTrue(check_alert_threshold(40, 35))
        self.assertFalse(check_alert_threshold(30, 35))

if __name__ == '__main__':
    unittest.main()
