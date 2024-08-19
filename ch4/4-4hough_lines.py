import cv2 as cv 
import sys
import numpy as np

img = cv.imread('road.jpg')
if img is None:
    sys.exit('파일을 찾을 수 없습니다.')

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
blur = cv.GaussianBlur(gray, (5, 5), 2, 2)
canny = cv.Canny(blur, 100, 200, 5)

rho, theta = 1,  np.pi / 180 # 0~180/180 -> 1도 단위로 나눔
lines = cv.HoughLinesP(canny, rho, theta, 10, minLineLength=20, maxLineGap=5) # 점의 개수 10개 이상, 적어도 20개 이상의 픽셀들로 구성, 점 사이 gap 최대 5
# 주로 에지영상을 입력
# 직선으로 판단할 threshold

if lines is not None:
    for line in lines:    # 검출된 선 그리기
        print(line)
        x1, y1, x2, y2 = line[0]
        len = np.sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2))
        print(len)
        cv.line(img, (x1,y1), (x2, y2), (0,255,0), 2)

cv.imshow("image", img)

cv.waitKey()
cv.destroyAllWindows()