# Color-Detection-using-Python
## Overview

This project is a real-time color identification system that uses a webcam to capture video and identify the color of a pixel selected by mouse click. It leverages OpenCV for video capture and display, and Pandas to process a color dataset (`colors.csv`) containing RGB values, color names, and hex codes. The system calculates the closest matching color based on RGB values using a Manhattan distance metric and displays the color name, hex code, and RGB values on the video feed. Designed to run on a local machine with a webcam, the project is lightweight and user-friendly, requiring a CSV file with color data.

## Features

- **Real-Time Video Processing**: Captures and processes live webcam feed, displaying the selected color and its details.
- **Color Matching**: Identifies the closest color name and hex code from a CSV dataset using Manhattan distance.
- **Interactive Interface**: Allows users to click on the video feed to select a pixel and retrieve its RGB values.
- **Dynamic Text Display**: Shows color name, hex code, and RGB values on the video feed, with adaptive text color for readability.
- **Lightweight Implementation**: Uses minimal dependencies and a simple algorithm for efficient performance.
- **Error Handling**: Handles missing or invalid color data gracefully by finding the closest match.

## Requirements

To run this project, ensure you have the following dependencies installed:

- Python 3.8+
- numpy
- pandas
- opencv-python (cv2)
- imutils

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Tarun0744/color_detection.git
   cd color_detection
   ```

2. **Install Dependencies**:
   Install the required Python packages using pip:
   ```bash
   pip install numpy pandas opencv-python imutils
   ```

3. **Set Up Color Data**:
   - Place a `colors.csv` file in the project directory.
   - The CSV should have columns: `color`, `color_name`, `hex`, `R`, `G`, `B` (no header).
   - Example row: `red,Red,#FF0000,255,0,0`
   - A sample `colors.csv` can be obtained from online color datasets or created manually.

## Usage

1. **Prepare the Color Dataset**:
   - Ensure the `colors.csv` file is in the project directory with the correct format.

2. **Run the Script**:
   - Execute the `color_identification.py` script:
     ```bash
     python color_identification.py
     ```
   - The script will:
     - Load the color data from `colors.csv`.
     - Start a live video feed using the webcam.
     - Display color information for the pixel clicked by the user.

3. **Perform Color Identification**:
   - Click on any point in the video feed to select a pixel.
   - The script retrieves the RGB values of the clicked pixel and matches them to the closest color in the dataset.

4. **Interact with the System**:
   - The video feed displays a colored rectangle showing the selected color, along with the color name, hex code, and RGB values.
   - Outputs are displayed in real-time; no files are saved.

5. **View Results**:
   - The color information (name, hex, RGB) is shown on the video feed.
   - Press the `Esc` key to exit the video feed.

## Project Structure

```
color_identification/
├── color_detecttion.py     # Main script for real-time color identification
├── colors.csv              # Color dataset file (to be provided by user)
└── README.md               # This file
```

## Notes

- **Webcam Requirement**: A functional webcam is required for real-time video capture. Ensure it is properly connected and accessible.
- **Color Dataset**: The `colors.csv` file must exist and follow the expected format. Missing or incorrect data may lead to inaccurate color matching.
- **Performance**: The system is lightweight but depends on the size of the color dataset for matching speed. Large datasets may slightly slow down processing.
- **Text Readability**: The script adjusts text color (white or black) based on the brightness of the selected color (R+G+B >= 600) for better visibility.
- **Limitations**: The Manhattan distance metric is simple and may not always find the perceptually closest color. More advanced metrics (e.g., Delta E) could improve accuracy.
- **Error Handling**: The script assumes the `colors.csv` file is present and valid. Add error handling for missing files if needed.

## Example

To identify colors using the webcam:
1. Place a valid `colors.csv` file in the project directory.
2. Run `color_detection.py`.
3. The webcam feed will start, displaying the live video.
4. Click on any point in the video feed to select a pixel.
5. The feed will display the color name, hex code, and RGB values, e.g., `Red   Hex=#FF0000   R=255 G=0 B=0`.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue for bug reports, feature requests, or improvements.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Built using OpenCV for webcam capture and image processing.
- Utilizes Pandas for efficient handling of the color dataset.
- Inspired by real-time computer vision applications for color detection.
