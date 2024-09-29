
import unittest
from object_detection import load_model

class TestObjectDetection(unittest.TestCase):
    def test_load_model(self):
        model = load_model()
        self.assertIsNotNone(model)  # Ensure model loads properly

if __name__ == "__main__":
    unittest.main()
