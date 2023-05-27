number_plate.py
# Convert image to grayscale
 # Apply Gaussian blur
  # Apply Canny edge detection
 # Find contours
# Filter contours based on area and aspect ratio
min_area = 500
    max_area = 5000
    aspect_ratio_range = (2.5, 6)
    valid_contours = []
    for contour in contours:
        area = cv2.contourArea(contour)
        x, y, w, h = cv2.boundingRect(contour)
        aspect_ratio = w / float(h)
        if area > min_area and area < max_area and aspect_ratio > aspect_ratio_range[0] and aspect_ratio < aspect_ratio_range[1]:
            valid_contours.append(contour)
 # Draw bounding rectangles around valid contours
# Load image
# Find number plate
# Display result
