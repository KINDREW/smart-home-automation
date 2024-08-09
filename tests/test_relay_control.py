import unittest
from src import relay_control

class TestRelayControl(unittest.TestCase):
    def test_control_appliance(self):
        relay_control.control_appliance("on")
        relay_control.control_appliance("off")

if __name__ == '__main__':
    unittest.main()
