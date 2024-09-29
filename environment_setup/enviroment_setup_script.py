import os

# Required libraries
libraries = [
    "opencv-python",
    "tensorflow",
    "torch",
    "pyttsx3",
    "numpy",
    "Pillow",
    "matplotlib",
]

# Install libraries
for library in libraries:
    os.system(f"pip install {library}")

print("Environment setup complete. Required libraries installed.")
