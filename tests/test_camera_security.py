import unittest
from src import camera_security

class TestCameraSecurity(unittest.TestCase):
    def test_capture_image(self):
        result = camera_security.capture_image()
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()
