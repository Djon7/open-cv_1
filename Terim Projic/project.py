import cv2
import numpy as np

def find_number_plate(image):
   
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

   
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    
    edges = cv2.Canny(blurred, 50, 150)

   
    contours, _ = cv2.findContours(edges.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

   
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

  
    for contour in valid_contours:
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

    return image


image = cv2.imread('car.jpg')


result = find_number_plate(image)


cv2.imshow('Number Plate Detection', result)
cv2.waitKey(0)
cv2.destroyAllWindows()
