import cv2 as cv

img=cv.imread('mot_color70.jpg') # 영상 읽기
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)

sift=cv.SIFT_create() 
kp,des=sift.detectAndCompute(gray,None)
print(len(kp))
print(kp[0].pt, kp[0].size, kp[0].octave, kp[0].angle)
# 0번째 kp의 위치정보, 사이즈, 옥타브, 그래디언트 각도
print(des[0])  # 8개씩 총 128개

# gray=cv.drawKeypoints(gray,kp,None,flags=cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
gray=cv.drawKeypoints(gray,kp,None,flags=cv.DRAW_MATCHES_FLAGS_DEFAULT)  # 특징점만
cv.imshow('sift', gray)

k=cv.waitKey()
cv.destroyAllWindows()