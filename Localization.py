import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread("number.jpg")

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# img_blur = cv2.GaussianBlur(img_gray, (3,3), 5)

# plt.imshow(img_blur)
# plt.show()
#########################################################################################################
# img_th = cv2.adaptiveThreshold(255-img_gray, 255,
#                                cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV,15,20)
# adaptiveThreshold(src, maxValue, adaptiveMethod, thresholdType, blockSize, C)
# src : 그레이스케일 이미지
# maxValue – 기준값을 넘었을 때 적용할 값
# adaptiveMethod : 영역 내에서 기준값을 계산하는 방법.
            #예) ADAPTIVE_THRESH_MEAN_C: 영역 내의 평균값에 C를 뺀 값을 기준값으로 사용
            #예) ADAPTIVE_THRESH_GAUSSIAN_C: 영역에 추후 설명할 가우시안 블러를 적용한 후 C를 뺀 값을 기준값으로 사용
# thresholdType : 임계처리 유형
        # THRESH_BINARY : 기준값을 넘으면 최대값 아니면 0
        # THRESH_BINARY_INV : 기준값을 넘으면 0 아니면 최대값
        # THRESH_TRUNC : 기준값을 넘으면 기준값 아니면 최대값
        # THRESH_TOZERO : 기준값을 넘으면 원래값 아니면 0
        # THRESH_TOZERO_INV : 기준값을 넘으면 0 아니면 원래값
# blockSize : 임계처리를 적용할 영역의 크기
# C : 평균이나 가중평균에서 차감할 값
#
# plt.imshow(img_th)
# plt.show()
#########################################################################################################
ret, img_th = cv2.threshold(img_gray, 80, 230, cv2.THRESH_BINARY_INV)
# plt.imshow(img_th)
# plt.show()
image, contours, hierachy= cv2.findContours(img_th.copy(),
                                 cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
# plt.imshow(image)
# plt.show()

#이미지 첫번째꺼
# #########################################################################################################
rects = [cv2.boundingRect(each) for each in contours]

# tmp = [w*h for (x,y,w,h) in rects]
rects = [(x,y,w,h) for (x,y,w,h) in rects if (x>240)]
print(rects)
for rect in rects:
    # Draw the rectangles


    cv2.rectangle(img, (rect[0], rect[1]),
                  (rect[0] + rect[2], rect[1] + rect[3]), (0, 255, 0),3)

    # print(rects)
plt.imshow(img)
plt.show()
# rectangle 는 이미지주변에 사각형 만드는것
# 그려질이미지,(사각형의시작점),(시작점과대각선에있는사각형의끝점,(색 R,G,B),(선굵기))
# plt.imshow(img)
# plt.show()

img_result = []
img_for_class = cv2.imread("number.jpg")
i=0
for rect in rects:


    img_result.append(img_for_class[rect[1]-15 : rect[1] + rect[3]+15 ,
                                    rect[0]-15 : rect[0] + rect[2]+15 ])
    # plt.imshow(img_result[i])
    # plt.show()
    i += 1
    if i >=len(rects):
        break

