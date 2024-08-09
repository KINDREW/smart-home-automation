import unittest
from src import temperature_humidity

class TestTemperatureHumidity(unittest.TestCase):
    def test_monitor_temperature_humidity(self):
        result = temperature_humidity.monitor_temperature_humidity()
        self.assertIsNotNone(result)

if __name__ == '__main__':
    unittest.main()
