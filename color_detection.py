# Import required libraries for numerical operations, data handling, computer vision, and image processing
import numpy as np
import pandas as pd
import cv2
import imutils

# Initialize the webcam feed (default camera, index 0)
camera = cv2.VideoCapture(0)

# Initialize variables to store RGB values and mouse click coordinates
r = g = b = xpos = ypos = 0

# Load the colors dataset from a CSV file, defining column names for color data
index = ['color', 'color_name', 'hex', 'R', 'G', 'B']
df = pd.read_csv('colors.csv', names=index, header=None)

# Function to find the closest color name based on RGB values
def getColorName(R, G, B):
    # Initialize minimum distance for color comparison
    minimum = 10000
    cname = ""
    # Iterate through the colors dataset to find the closest matching color
    for i in range(len(df)):
        # Calculate the Euclidean distance between input RGB and dataset RGB
        d = abs(R - int(df.loc[i, "R"])) + abs(G - int(df.loc[i, "G"])) + abs(B - int(df.loc[i, "B"]))
        if d <= minimum:
            minimum = d
            # Store the color name and hex code of the closest match
            cname = df.loc[i, 'color_name'] + '   Hex=' + df.loc[i, 'hex']
    return cname

# Callback function to capture mouse click events and extract RGB values
def identify_color(event, x, y, flags, param):
    global b, g, r, xpos, ypos
    # Update coordinates and RGB values when a mouse event occurs
    if event == cv2.EVENT_LBUTTONDOWN:
        xpos = x
        ypos = y
        # Extract RGB values at the clicked pixel
        b, g, r = frame[y, x]
        b = int(b)
        g = int(g)
        r = int(r)

# Create a window for displaying the video feed
cv2.namedWindow('image')
# Set the mouse callback function to handle mouse interactions
cv2.setMouseCallback('image', identify_color)

# Main loop to process video frames
while True:
    # Capture a frame from the webcam
    (grabbed, frame) = camera.read()
    # Resize the frame to a fixed width for consistent display
    frame = imutils.resize(frame, width=900)
    # Create a 5x5 kernel for potential image processing (currently unused)
    kernal = np.ones((5, 5), "uint8")
    
    # Draw a rectangle at the top of the frame filled with the selected RGB color
    cv2.rectangle(frame, (20, 20), (800, 60), (b, g, r), -1)
    
    # Get the color name and prepare text to display RGB and color information
    text = getColorName(b, g, r) + '   R=' + str(r) + ' G=' + str(g) + ' B=' + str(b)
    # Display the text on the frame with white color for visibility
    cv2.putText(frame, text, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2, cv2.LINE_AA)
    
    # If the color is too bright (sum of RGB >= 600), use black text for readability
    if (r + g + b) >= 600:
        cv2.putText(frame, text, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 0), 2, cv2.LINE_AA)
    
    # Display the processed frame in the window
    cv2.imshow('image', frame)
    
    # Exit the loop if the 'Esc' key is pressed
    if cv2.waitKey(20) & 0xFF == 27:
        break

# Release the webcam resource
camera.release()
# Close all OpenCV windows
cv2.destroyAllWindows()
