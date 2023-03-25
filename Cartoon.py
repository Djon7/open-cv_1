import cv2
import numpy as np

# 입력 이미지 로드
img = cv2.imread("C:/Users/lenovo/Desktop/113.jpg")

# 그레이스케일로 변환
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 가우시안 블러 적용
gray = cv2.medianBlur(gray, 5)

# 엣지 검출
edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)

# 컬러 이미지로 변환
color = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# 엣지 정보를 사용하여 스타일화
stylized_img = cv2.stylization(color, sigma_s=150, sigma_r=0.25)

# 엣지 정보 추가
cartoon = cv2.bitwise_and(stylized_img, stylized_img, mask=edges)

# 결과 이미지 화면에 보여주기
cv2.imshow('Cartoonized Image', cartoon)
cv2.waitKey(0)
cv2.destroyAllWindows()
