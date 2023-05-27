
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

# image 1

![image_2023-05-27_17-03-15](https://github.com/Djon7/open-cv_1/assets/128918874/e6150604-d5f1-4328-bb14-8e1bd36f50d1)

# image Result 2

![car](https://github.com/Djon7/open-cv_1/assets/128918874/910dae75-c92f-4744-9036-81b69652cd6d)

