import unittest
from src import voice_control

class TestVoiceControl(unittest.TestCase):
    def test_execute_voice_command(self):
        voice_control.execute_voice_command("turn on the light")
        voice_control.execute_voice_command("turn off the light")

if __name__ == '__main__':
    unittest.main()
