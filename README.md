# Hand_Gesture_Presentation

# Gesture-Controlled Presentation

This project enables you to control a presentation using hand gestures captured by a webcam. Utilizing Python and OpenCV, the system detects hand landmarks and interprets specific gestures for navigating through presentation slides.

## Features

- Slide Navigation:** Easily navigate through presentation slides using left and right gestures.
- Annotation Mode:** Draw on slides by pointing with your index finger while making a specific gesture.
- Undo Annotations:** Effortlessly undo the last drawn annotation using a specific gesture.

## Getting Started

### Prerequisites

- Python 3.x
- OpenCV
- cvzone library (included in the project)

### Installation

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/your-username/gesture-controlled-presentation.git
   ```

2. Install the required dependencies:

   ```bash
   pip install opencv-python
   ```

### Usage

1. Run the `main.py` script:

   ```bash
   python main.py
   ```

2. Utilize your webcam to control the presentation slides:
   - Swipe left with one finger to go to the previous slide.
   - Swipe right with one finger to go to the next slide.
   - Point with your index finger to draw on the current slide.
   - Swipe down with one finger to undo the last drawn annotation.

3. Press 'Q' to exit the application.

## Customization

- **Slide Images:** Place your presentation images in the "Presentation" folder.
- **Gesture Threshold:** Adjust the `gestureThreshold` parameter in the code to set the height threshold for hand detection.

## Acknowledgments

- This project uses the [cvzone](https://github.com/cvzone/cvzone) library for hand tracking.

## Contributing

Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue or create a pull request.

---

Feel free to customize this README further based on your project's specifics. Include more details about the project structure, dependencies, and any other relevant information.
