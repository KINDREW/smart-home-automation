import unittest
from src import motion_detection

class TestMotionDetection(unittest.TestCase):
    def test_detect_motion(self):
        result = motion_detection.detect_motion()
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()
