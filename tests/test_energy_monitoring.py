import unittest
from src import energy_monitoring

class TestEnergyMonitoring(unittest.TestCase):
    def test_monitor_energy_usage(self):
        result = energy_monitoring.monitor_energy_usage()
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()
