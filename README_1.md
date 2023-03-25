입력 이미지를 로드하고, 가우시안 블러(Gaussian Blur)를 적용합니다. 가우시안 블러는 이미지의 노이즈를 제거하고, 이미지를 부드럽게 만드는 역할을 합니다.

img = cv2.imread('input_image.jpg')
blur = cv2.GaussianBlur(img, (3,3), 0)

엣지 검출(Edge Detection)을 수행합니다. 이 코드에서는 캐니 엣지 검출(Canny Edge Detection) 함수를 사용합니다.

edges = cv2.Canny(blur, 100, 200)

Canny() 함수의 두 번째와 세 번째 인자는 각각 최소 및 최대 임계값으로, 이 임계값에 따라 엣지가 검출됩니다. 두 번째 인자인 최소 임계값은 낮은 엣지 값을, 세 번째 인자인 최대 임계값은 높은 엣지 값을 나타냅니다.

마지막으로, bitwise_and() 함수를 사용하여 엣지 정보를 스타일화된 이미지에 추가합니다.

cartoon = cv2.bitwise_and(stylized, stylized, mask=edges)

위 코드에서 mask 인자는 edges 이미지를 마스크로 사용하여 스타일화된 이미지와 엣지를 결합합니다. 이렇게 하면 엣지를 따라 스타일화된 이미지가 만화 스타일로 변환됩니다.