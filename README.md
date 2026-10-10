# Age Prediction App

A simple desktop application for estimating a person's age from a photo. The app opens an image, detects a face using OpenCV, and passes it to a pre-trained neural network to predict the age.

## Features

- opens an image through a file dialog;
- detects faces in the uploaded photo;
- preprocesses the image for the model;
- displays the predicted age in a graphical interface.

## Tech Stack

- Python
- Tkinter
- OpenCV
- Pillow
- NumPy
- TensorFlow / Keras

## Project Files

- `main.py` — application logic and UI
- `Gender_and_Age.keras` — trained model
- `Gender_and_Age.h5` — backup model file

## Installation

1. Make sure Python 3.9+ is installed.
2. Install the dependencies:

```bash
pip install tensorflow opencv-python pillow numpy
```

3. Run the application:

```bash
python main.py
```

## Usage

1. Click the `Choose image` button.
2. Select an image containing a face.
3. The application will display the estimated age if a face is detected and processed successfully.

## Note

For the app to work correctly, the `Gender_and_Age.keras` model file must be present in the project root directory.
