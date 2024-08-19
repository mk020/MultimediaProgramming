import skimage  # scikit-image 설치
import numpy as np
import cv2 as cv

orig=skimage.data.horse()   # 배경 1, 물체0(black)
img=255-np.uint8(orig)*255  # 0과 1 -> 0과 255 -> 255와 0 으로 바꿔줌
cv.imshow('Horse',img)

contours,hierarchy=cv.findContours(img,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_NONE)

img2=cv.cvtColor(img,cv.COLOR_GRAY2BGR)		# 컬러 디스플레이용 영상
cv.drawContours(img2,contours,-1,(255,0,255),2)
cv.imshow('Horse with contour',img2)

contour=contours[0]
print(contour.shape)

m=cv.moments(contour)				# 몇 가지 특징
print(m)

area=cv.contourArea(contour)
cx,cy=m['m10']/m['m00'],m['m01']/m['m00']
perimeter=cv.arcLength(contour,True)
roundness=(4.0*np.pi*area)/(perimeter*perimeter)
print('면적=',area,'\n중점=(',cx,',',cy,')','\n둘레=',perimeter,'\n둥근 정도=',roundness)

img3=cv.cvtColor(img,cv.COLOR_GRAY2BGR)		# 컬러 디스플레이용 영상

contour_approx=cv.approxPolyDP(contour,8,True)	# 직선 근사, 최대 8까지 떨어짐
cv.drawContours(img3,[contour_approx],-1,(0,255,0),2)
print(contour_approx.shape)  # 픽셀 개수(픽셀들을 이어 직선)
contour_approx=cv.approxPolyDP(contour,20,True)	# 직선 근사
cv.drawContours(img3,[contour_approx],-1,(255,255,0),2)
print(contour_approx.shape)

hull=cv.convexHull(contour)			# 볼록 헐
cv.drawContours(img3,[hull],-1,(0,0,255),2)  # 배열
print(hull.shape)

rehull=hull.reshape(1,hull.shape[0],hull.shape[2])  # reshape
cv.drawContours(img3,rehull,-1,(0,0,255),2)

cv.imshow('Horse with line segments and convex hull',img3)

cv.waitKey()
cv.destroyAllWindows()