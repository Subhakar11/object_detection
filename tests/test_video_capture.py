import unittest
from video_capture import start_video_capture

class TestVideoCapture(unittest.TestCase):
    def test_video_capture(self):
        # Here, you would generally want to test the output frame or any exceptions
        try:
            start_video_capture()
            self.assertTrue(True)  # If the function runs without error
        except Exception as e:
            self.fail(f"Video capture failed with exception: {e}")

if __name__ == "__main__":
    unittest.main()
